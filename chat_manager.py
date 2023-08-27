import typing
import asyncio
import os
import io

from aiogram import Bot
from aiogram import types
from aiogram.types import base
from aiogram.types import InputFile
from aiogram.types.chat import ChatActions
from aiogram.utils.exceptions import MessageNotModified, BadRequest, InlineKeyboardExpected
import logging

import pickle
import datetime

from states.states import State, USER
from buttons.buttons import Buttons
from utils import utils

from data.storage import DatabaseManager
db = DatabaseManager()

class History:
    def __init__(self):
        self.temporary_messages = []
        self.unhandled_messages = []
        self.lastInteractionDate = datetime.datetime.now()
        self.main_message_id = 0
        self.photo_messages = set()
        self.states = []
        self.data = {}

class Chat:
    def __init__(self, cid: int, bot: Bot):
        self.cid = cid
        self.bot = bot
        self.history = History()
    
    async def setState(self, state: State, data='-'):
        for m in self.history.temporary_messages:
            try:
                await self.bot.delete_message(self.cid, m)
            except Exception as e:
                logging.error(f'Cant delete message {m} because ')

        self.history.temporary_messages = []
        self.history.states.append([state.ID, data])
        db.setState(self.cid, state.ID)

    def isNewUser(self):
        jd = db.fetchone('SELECT joining_date FROM users WHERE cid = ?', (self.cid,))[0]
        jd = utils.str2dt(jd)
        if utils.now() - jd < datetime.timedelta(hours=1):
            return True
        return False

    def getState(self):
        return db.getState(self.cid)
    
    def getSubscriptionLevel(self):
        return db.getUserSubscription(self.cid)
    
    # def setSubscriptionLevel(self, sub_level):
    #     db.query('UPDATE users SET sub')

    async def back(self, message: types.Message):
        self.history.states.pop()
        state = self.history.states.pop()
        id, data = state
        if data == '-':
            await State.get(id)(message)
        else:    
            await State.get(id)(message,data)

    async def send(self, text: base.String = None,
                        reply_markup: typing.Union[Buttons, None] = None,
                        photo: typing.Union[base.InputFile, base.String] = None,
                        temporary: bool = False,
                        main_message: bool = False,
                        parse_mode: typing.Union[base.String, None] = None,
                        disable_notification: typing.Union[base.Boolean, None] = None ):
        msg = None

        markup = reply_markup
        if reply_markup and type(reply_markup) == Buttons:
            markup = reply_markup.getMarkup()

        if photo is not None:
            if type(photo) == bytes or type(photo) == str:
                msg = await self.bot.send_photo(self.cid, photo, text,parse_mode, disable_notification,reply_markup=markup)
            else:
                msg = await self.bot.send_animation(self.cid, photo,caption= text,parse_mode= parse_mode,disable_notification= disable_notification,reply_markup=markup)
            self.history.photo_messages.add(msg.message_id)
        else:
            msg = await self.bot.send_message(self.cid, text, parse_mode,disable_notification = disable_notification, reply_markup=markup)
        
        if temporary:
            self.history.temporary_messages.append(msg.message_id)

        self.history.lastInteractionDate = msg.date
        if main_message:
            self.history.main_message_id = msg.message_id
    
        return msg
    
    async def edit(self, text: base.String = None,
            reply_markup: typing.Union[Buttons, None] = None,
            photo: typing.Union[base.InputFile, base.String] = None,
            message_id: int = None,
            parse_mode: typing.Union[base.String, None] = None) -> types.Message or base.Boolean:
        
        is_main_message = not message_id
        if is_main_message:
            message_id = self.history.main_message_id

        if reply_markup and type(reply_markup) == Buttons:
            reply_markup = reply_markup.getMarkup()

        try:
            msg = await self.edit_impl(text, reply_markup, photo, message_id, parse_mode)
        except:
            msg = await self.send(text, reply_markup, photo, parse_mode=parse_mode, main_message=is_main_message)
        if msg:
            if is_main_message:
                self.history.main_message_id = msg.message_id
            self.history.lastInteractionDate = msg.edit_date if msg.edit_date else msg.date
    
        return msg
    
    async def edit_impl(self, text: base.String = None,
                reply_markup: typing.Union[types.InlineKeyboardMarkup, None] = None,
                photo: typing.Union[base.InputFile, base.String] = None,
                message_id: int = None,
                parse_mode: typing.Union[base.String, None] = None) -> types.Message or base.Boolean:

        if not text and not photo and reply_markup:
            return await self.bot.edit_message_reply_markup(self.cid, message_id, reply_markup=reply_markup)
        

        if message_id in self.history.photo_messages:
            await self.bot.delete_message(chat_id=self.cid, message_id=message_id)
            return await self.send(text,reply_markup,photo, False,not message_id, parse_mode)

        else:
            try:
                if photo:
                    raise ValueError()
                return await self.bot.edit_message_text(chat_id=self.cid,
                                                                message_id=message_id,
                                                                text=text,
                                                                reply_markup=reply_markup,
                                                                parse_mode=parse_mode)
            except:
                if text:
                    await self.bot.delete_message(chat_id=self.cid, message_id=message_id)
                    return await self.send(text,reply_markup, photo, False, not message_id, parse_mode)
                else:
                    return await self.bot.edit_message_reply_markup(self.cid, message_id, reply_markup=reply_markup)

    async def pre_process_update(self, update: types.Update):
        if update.callback_query:
            message = update.callback_query.message
        elif update.message:
            message = update.message
        elif update.my_chat_member and update.my_chat_member.new_chat_member.status=='kicked':
            db.query('UPDATE users SET account_state=1 WHERE cid=?',(update.my_chat_member.chat.id,))
            logging.info(f'User {update.my_chat_member.chat.first_name}:{update.my_chat_member.chat.id} blocked the bot.')
            return
        else:
            logging.error("Unknown update type on_pre_process_update")
            logging.info(update.as_json())
            return
        
        self.history.unhandled_messages.append(message.message_id)
        if not message.from_user.is_bot:
            self.history.temporary_messages.append(message.message_id)

    def post_process_update(self, update: types.Update):
        if update.callback_query:
            message = update.callback_query.message
        elif update.message:
            message = update.message
        else:
            logging.error("Unknown update type on_post_process_update")
            logging.info(update.as_json())
            return

        if len(self.history.unhandled_messages):
            logging.debug(f"Messages {self.history.unhandled_messages} from {self.cid} are not handled")
        
        self.history.unhandled_messages.clear()


class ChatManager:
    def __init__(self, bot):
        self.bot = bot
        self.chats = {}
    
    def save_old_chats(self):
        keys = list(self.chats.keys())
        for cid in keys:
            chat = self[cid]
            if datetime.datetime.now() - chat.history.lastInteractionDate > datetime.timedelta(minutes=5):
                try:
                    self.save(cid)
                except Exception as e:
                    print(e)
                    logging.error(f'Cant save chat {cid}')
            
    def save_all(self):
        chatids = list(self.chats.keys())
        for cid in chatids:
            self.save(cid)

    def __getitem__(self, cid: int) -> Chat:
        if cid not in self.chats.keys():
            if f'{cid}.chat' in os.listdir('chats'):
                self.load(cid)
            else:
                self.chats[cid] = Chat(cid, self.bot)

        return self.chats[cid]

    def save(self, cid):
        if cid in self.chats.keys():
            chat = self[cid]
            with open(f'chats/{cid}.chat',mode='wb') as chatFile:
                pickle.dump(chat.history, chatFile)
            self.chats.pop(cid)
    
    def load(self, cid):
        with open(f'chats/{cid}.chat',mode='rb') as chatFile:
            if cid not in self.chats.keys():
                self.chats[cid] = Chat(cid, self.bot)
            self.chats[cid].history = pickle.load(chatFile)

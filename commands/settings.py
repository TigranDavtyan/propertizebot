from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER, State
from buttons.buttons import setActionFor, Buttons
import datetime
from utils import utils
from listam import User as LUser
import config
import logging
import asyncio

logger = logging.getLogger()

@setActionFor(USER.SETTINGS.INFO)
async def settings_info(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    settings = db.getUserSettings(cid)
    renews = settings['renews']
    
    renews_sorted = []
    for time, limit in renews.items():
        hour, minute = time.split(':')
        renews_sorted.append([datetime.time(int(hour), int(minute)), limit])

    renews_sorted.sort(key=lambda x: x[0])
    markup = Buttons()

    markup.add(P.add(cid), USER.SETTINGS.ADD_TIME)
    for renew in renews_sorted:
        time, limit = renew
        timeKey = time.strftime('%H:%M')
        markup.row([[timeKey, USER.SETTINGS.CHANGE_TIME, timeKey],[limit, USER.SETTINGS.CHANGE_LIMIT, timeKey],[P.delete(cid), USER.SETTINGS.DELETE_TIME, timeKey]])
    
    markup.add(P.menu(cid), USER.MAIN_MENU)

    await chat.edit(P.times_info(cid), markup)
    await chat.setState(USER.SETTINGS.INFO)

    
@setActionFor(USER.SETTINGS.ADD_TIME)
async def settings_add_time(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    await chat.edit(P.ask_new_time(cid))
    await chat.setState(USER.SETTINGS.ADD_TIME)


@setActionFor(USER.SETTINGS.HANDLE_NEW_TIME)
async def settings_handle_new_time(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    if not message.from_user.is_bot:
        if not utils.validateTime(message.text):
            await chat.send(P.wrong_format(cid), temporary=True)
            return
        hour,minute = message.text.split(':')
        if len(hour) == 1:
            time = f'0{hour}:{minute}'
        else:
            time = message.text
        chat.history.data['time'] = time

    await chat.edit(P.ask_new_limit(cid))
    await chat.setState(USER.SETTINGS.HANDLE_NEW_TIME)


@setActionFor(USER.SETTINGS.HANDLE_NEW_LIMIT)
async def settings_handle_new_time(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    try:
        limit = int(message.text)
        if limit < 0:
            raise ValueError()
    except:
        await chat.send(P.wrong_format(cid), temporary=True)
        return
    
    chat.history.data['limit'] = limit
    settings = db.getUserSettings(cid)

    settings['renews'][chat.history.data['time']] = limit
    db.setUserSettings(cid,settings)

    await chat.send(P.time_added_successfully(cid), temporary=True)
    await asyncio.sleep(1)
    await State.get(USER.SETTINGS.INFO)(message)




@setActionFor(USER.SETTINGS.CHANGE_TIME)
async def settings_change_time(message: Message, time):
    cid, chat = message.chat.id, cm[message.chat.id]
    chat.history.data['oldTime'] = time
    await chat.setState(USER.SETTINGS.CHANGE_TIME, time)
    await chat.send(P.change_time(cid), temporary=True)

@setActionFor(USER.SETTINGS.CHANGE_TIME_HANDLE)
async def settings_change_time_handle(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    if not utils.validateTime(message.text):
        await chat.send(P.wrong_format(cid), temporary=True)
        return
    
    settings = db.getUserSettings(cid)
    renews = settings['renews']
    limit = renews.pop(chat.history.data['oldTime'])
    
    hour,minute = message.text.split(':')
    if len(hour) == 1:
        time = f'0{hour}:{minute}'
    else:
        time = message.text

    renews[time] = limit
    settings['renews'] = renews
    db.setUserSettings(cid,settings)
    
    await chat.send(P.time_changed_successfully(cid), temporary=True)
    await asyncio.sleep(1)
    await State.get(USER.SETTINGS.INFO)(message)




@setActionFor(USER.SETTINGS.CHANGE_LIMIT)
async def settings_change_limit(message: Message, time):
    cid, chat = message.chat.id, cm[message.chat.id]
    chat.history.data['oldTime'] = time
    await chat.setState(USER.SETTINGS.CHANGE_LIMIT, time)
    await chat.send(P.change_limit(cid), temporary=True)

@setActionFor(USER.SETTINGS.CHANGE_LIMIT_HANDLE)
async def settings_change_limit_handle(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]

    try:
        limit = int(message.text)
        if limit < 0:
            raise ValueError()
    except:
        await chat.send(P.wrong_format(cid), temporary=True)
        return
    
    settings = db.getUserSettings(cid)
    renews = settings['renews']
    renews[chat.history.data['oldTime']] = limit
    settings['renews'] = renews
    db.setUserSettings(cid,settings)

    await chat.send(P.limit_changed_successfully(cid), temporary=True)
    await asyncio.sleep(1)
    await State.get(USER.SETTINGS.INFO)(message)


@setActionFor(USER.SETTINGS.DELETE_TIME)
async def settings_delete_time(message: Message, time):
    cid, chat = message.chat.id, cm[message.chat.id]

    settings = db.getUserSettings(cid)
    renews = settings['renews']
    renews.pop(time)

    settings['renews'] = renews
    db.setUserSettings(cid,settings)

    await State.get(USER.SETTINGS.INFO)(message)
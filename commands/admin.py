import utils.utils as utils
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, InlineKeyboardMarkup
from buttons.buttons import *
from config import ADMIN_CHAT_ID
from phrases import phrases as P
from loader import *
from notifications import to_users
from states.states import ADMIN, GENERAL, USER, State
import logging
from notifications import broadcast
import re
import datetime

logger = logging.getLogger()

@setActionFor(ADMIN.DECLINE_PAYMENT)
async def decline_user_payment(message : Message, user_id):
    cid, chat = message.chat.id, cm[message.chat.id]
    user_id = int(user_id)
    await to_users.payment_declined(user_id)
    await bot.edit_message_reply_markup(cid, message.message_id, reply_markup= InlineKeyboardMarkup())


async def prolong_subscription(user_id, days):
    old_sub_end = db.fetchone('SELECT subscription_end FROM users WHERE cid=?',(user_id,))[0]
    old_sub_end = utils.str2dt(old_sub_end)

    if old_sub_end == '2025-01-01 00:00:00':
        new_sub_end = utils.now().replace(hour=0,minute=0,second=0,microsecond=0) + datetime.timedelta(days=days+1)
    else:
        new_sub_end = utils.str2dt(old_sub_end) + datetime.timedelta(days=days)

    db.query('UPDATE users SET subscription = 1, subscription_end=? WHERE cid=?;', (new_sub_end, user_id))

    await cm[ADMIN_CHAT_ID].send(f'User <code>{user_id}</code> payment accepted!', temporary=True)
    logging.info(f'NOTIF: ADMIN - {ADMIN_CHAT_ID} accepted user {user_id} invoice')
    await to_users.subscription_prolonged(user_id, new_sub_end)



@setActionFor(ADMIN.ADD_6MONTHS)
async def approve_user_payment_6months(message : Message, user_id):
    cid, chat = message.chat.id, cm[message.chat.id]
    user_id = int(user_id)
    await prolong_subscription(user_id, 183)
    await bot.edit_message_reply_markup(cid, message.message_id, reply_markup= ReplyKeyboardRemove())
   

@setActionFor(ADMIN.ADD_12MONTHS)
async def approve_user_payment_6months(message : Message, user_id):
    cid, chat = message.chat.id, cm[message.chat.id]
    user_id = int(user_id)
    await prolong_subscription(user_id, 366)
    await bot.edit_message_reply_markup(cid, message.message_id, reply_markup= ReplyKeyboardRemove())


@setActionFor(ADMIN.MENU)
async def admin_menu(message: Message, is_main_message: bool = False):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    markup = Buttons()
    
    markup.add('Broadcast message', ADMIN.BROADCAST)
    markup.add('Activate PREMIUM', ADMIN.ACTIVATE_PREMIUM)
   
    if not message.from_user.is_bot or is_main_message:
        await chat.send(P.menu(cid), markup, main_message=is_main_message)
    else:
        await chat.edit(P.menu(cid), markup)

    await chat.setState(ADMIN.MENU)


# @setActionFor(ADMIN.BROADCAST)
# async def broadcast_message1(message: Message):
#     cid, chat = message.chat.id, cm[message.chat.id]

#     await chat.edit('Send a message to broadcast, you can include a link at the end like this "href=example.com"')
#     await chat.setState(ADMIN.BROADCAST)

# message_id = 0

# async def edit_broadcast_message(message: Message, id):
#     pattern = r"href=(.+)"
#     match = re.search(pattern, message.caption[1:])

#     if match:
#         link = match.group(1)
#         description = message.caption[0:match.span(1)[0]-4]

#         link_button = Buttons()
#         link_button.addLink(P.visit_website(0),  USER.LINK_CLICK, link)

#         await bot.edit_message_caption(message.chat.id, id, caption=description, reply_markup=link_button.getMarkup())



# @setActionFor(ADMIN.BROADCAST_HANDLE)
# async def broadcast_message2(message: Message):
#     global message_id
#     cid, chat = message.chat.id, cm[message.chat.id]

#     original_message = message

#     new_id = (await bot.copy_message(cid, cid, message.message_id,)).message_id

#     try:
#         await edit_broadcast_message(message, new_id)
#     except:
#         await chat.send(P.wrong_action(cid), temporary=True)
#         return
    
#     message = await bot.forward_message(ad_channel, cid, new_id)
#     message_id = message.message_id

#     await chat.setState(ADMIN.BROADCAST_HANDLE)
#     await chat.send('Are you sure? type "yes" or anything else.', temporary=True) 


# @setActionFor(ADMIN.BROADCAST_CONFIRM)
# async def broadcast_message3(message: Message):
#     global message_id
#     cid, chat = message.chat.id, cm[message.chat.id]

#     if message.text.lower() == 'yes':
#         await chat.send('Sending messages...')
#         results = await broadcast.broadcast_users(ad_channel, message_id, False)
#         nMessages = 0
#         for res in results.values():
#             nMessages += res
#         result_text = f'''Broadcasted {nMessages} messages
# Successfull      - {results[0]}
# Blocked          - {results[1]}
# Invalid user     - {results[2]}
# Deactivated user - {results[3]}
# TelegramAPIError - {results[4]}'''

#         await chat.send(result_text)
    
#         logger.info(result_text)
#         message_id = ''
#     else:
#         await chat.send('Stopping the broadcast')
#         await State.get(ADMIN.MENU)(message)
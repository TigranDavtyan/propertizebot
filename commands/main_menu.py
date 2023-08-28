from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER, GENERAL
from buttons.buttons import *

@setActionFor(USER.MAIN_MENU)
async def cmd_menu_user(message: Message, is_main_message: bool = False):
    cid = message.chat.id
    chat = cm[cid]

    markup = Buttons()

    password = db.fetchone('SELECT password FROM users WHERE cid = ?;', (cid,))[0]
    if password:
        markup.add(P.change_logpass(cid), USER.SIGNUP.INFO)
        markup.add(P.renew_now(cid), USER.ACTIONS.RENEW)
    else:
        markup.add(P.signup(cid), USER.SIGNUP.INFO)
    markup.add(P.subscription(cid), USER.SUBSCRIPTION.INFO)

    if not message.from_user.is_bot or is_main_message:
        await chat.send(P.menu(cid), markup, main_message=is_main_message)
    else:
        await chat.edit(P.menu(cid), markup)

    await chat.setState(USER.MAIN_MENU)
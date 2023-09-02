from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER
from buttons.buttons import setActionFor, Buttons
import datetime
from utils import utils
from listam import User as LUser
import config
import logging

logger = logging.getLogger()

@setActionFor(USER.SIGNUP.INFO)
async def signup_info(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    info = P.signup_info(cid)
    
    markup = Buttons(True)
    markup.add(P.signup(cid), USER.SIGNUP.LOGIN)

    await chat.edit(info, markup)

    await chat.setState(USER.SIGNUP.INFO)


@setActionFor(USER.SIGNUP.LOGIN)
async def login(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.edit(P.ask_for_login(cid), Buttons(True))

    await chat.setState(USER.SIGNUP.LOGIN)


@setActionFor(USER.SIGNUP.HANDLE_LOGIN)
async def handle_login(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    isphone = utils.isPhoneNumber(message.text)
    isemail = utils.isEmail(message.text)
    if not isphone and not isemail:
        await chat.send(P.wrong_format(cid))
        return
    if isphone:
        db.query('UPDATE users SET phone_number = ?, email = "" WHERE cid = ?',(message.text, cid))
    elif isemail:
        db.query('UPDATE users SET email = ?, phone_number = "" WHERE cid = ?',(message.text, cid))

    await chat.edit(P.ask_for_password(cid), Buttons(True))

    await chat.setState(USER.SIGNUP.HANDLE_LOGIN)


@setActionFor(USER.SIGNUP.HANDLE_PASSWORD)
async def handle_password(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]
    oldPassword = db.fetchone('SELECT password FROM users WHERE cid = ?',(cid,))[0]
    logger.info(f'Old password is {oldPassword} ;')
    db.query('UPDATE users SET password = ? WHERE cid = ?',(message.text, cid))

    user = LUser(cid)
    if user.login() == 200:
        markup = Buttons()
        markup.add(P.menu(cid), USER.MAIN_MENU)

        if not oldPassword:
            free_trial = utils.now() + datetime.timedelta(days=config.FREE_TRIAL_DAYS)
            db.query('UPDATE users SET subscription_end = ? WHERE cid = ?', (free_trial, cid))

        await chat.edit(P.successfull_login(cid), markup)
    else:
        await chat.edit(P.error_login(cid), Buttons(True))

    await chat.setState(USER.SIGNUP.HANDLE_PASSWORD)
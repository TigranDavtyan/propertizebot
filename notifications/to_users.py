import sys

import logging

import config
from aiogram.types import Message
from loader import *
from phrases import phrases as P
from utils import logging as lgm
from utils import utils
from buttons.buttons import Buttons, setActionFor
from states.states import USER

logger = logging.getLogger()

async def subscription_ended(cid):
    chat = cm[cid]
    await chat.send(P.subscription_end(cid), temporary=False)
    logger.info(f'User {cid} subscription ended.')

async def subscription_prolonged(user_id, new_sub_end):
    chat = cm[user_id]
    await chat.send(P.payment_successfull(user_id, new_sub_end.date()), temporary=False)
    logger.info(f'User {user_id} subscription prolonged to {new_sub_end}.')

async def payment_declined(user_id):
    chat = cm[user_id]
    await chat.send(P.payment_declined(user_id), temporary=False)
    logger.info(f'User {user_id} payment was declined')
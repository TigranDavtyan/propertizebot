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

@setActionFor(USER.SETTINGS.INFO)
async def settings_info(message: Message):
    cid, chat = message.chat.id, cm[message.chat.id]
    
    settings = db.getUserSettings(cid)
    
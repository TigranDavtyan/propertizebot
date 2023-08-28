from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER
from buttons.buttons import setActionFor, Buttons
import datetime
from utils import utils
from listam import User as LUser
import config

@setActionFor(USER.ACTIONS.RENEW)
async def renew_now(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]
    
    user = LUser.get(cid)
    
    res = await user.renewListings()
    if res == -1:
        await chat.send(P.cant_renew_for_30_mins(cid), temporary=True)
    else:
        await chat.send(P.renewd_n_items(cid, nRenews = user.nRenews), temporary = True)
    
    user.nRenews = 0
    user.nErrors = 0

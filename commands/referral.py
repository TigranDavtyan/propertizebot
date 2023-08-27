from loader import *
from aiogram.types import Message
from phrases import phrases as P
from states.states import USER
from buttons.buttons import setActionFor, Buttons
from config import BOT_USERNAME, BONUS_REFS, BONUS_DAYS_FOR_REFS
import datetime
from utils import utils

@setActionFor(USER.REFERRAL.INFO)
async def referral_info(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    hash_cid = utils.ref_code_hash(cid)
    nRefs = db.fetchone('SELECT COUNT(cid) FROM users WHERE referral_id=?',(hash_cid,))[0]
    ref_link = f't.me/{BOT_USERNAME}?start=ref{hash_cid}'

    info = P.referral_info(cid, BONUS_REFS, BONUS_DAYS_FOR_REFS, ref_link)

    if nRefs >= BONUS_REFS:
        bonus_days = nRefs // BONUS_REFS * BONUS_DAYS_FOR_REFS
        
        markup = Buttons(True)
        markup.add(P.get_referral_bonus(cid), USER.REFERRAL.GET_BOUNS)
        
        await chat.edit(info + '\n\n' + P.referral_bonus(cid, nRefs, bonus_days), markup)

    else:
        await chat.edit(info + '\n\n' + P.no_referral_bonus(cid, nRefs, BONUS_REFS, BONUS_DAYS_FOR_REFS), Buttons(True))
    
    await chat.setState(USER.REFERRAL.INFO)


@setActionFor(USER.REFERRAL.GET_BOUNS)
async def get_ref_bonus(message: Message, data = None):
    cid, chat = message.chat.id,cm[message.chat.id]

    hash_cid = utils.ref_code_hash(cid)
    nRefs = db.fetchone('SELECT COUNT(cid) FROM users WHERE referral_id=?',(hash_cid,))[0]

    bonus_days = nRefs // BONUS_REFS * BONUS_DAYS_FOR_REFS
    
    next_payment = db.fetchone('SELECT subscription_end FROM users WHERE cid=?',(cid,))[0]

    if next_payment == '2025-01-01 00:00:00':
        new_next_payment = utils.now().replace(hour=0,minute=0,second=0,microsecond=0) + datetime.timedelta(days=bonus_days+1)
    else:
        new_next_payment = utils.str2dt(next_payment) + datetime.timedelta(days=bonus_days)

    db.query('UPDATE users SET subscription=1, subscription_end=? WHERE cid=?',(new_next_payment, cid))

    nRefs = int(bonus_days / BONUS_DAYS_FOR_REFS * BONUS_REFS)
    db.query('''UPDATE users SET referral_id = referral_id || '000'
WHERE cid IN (SELECT cid FROM users WHERE referral_id = ? ORDER BY cid LIMIT ?)''', (hash_cid, nRefs))

    markup = Buttons()
    markup.add(P.menu(cid), USER.MAIN_MENU)
    await chat.edit(P.congratulate_bonus(cid, bonus_days), markup)
    await chat.setState(USER.REFERRAL.GET_BOUNS)
    
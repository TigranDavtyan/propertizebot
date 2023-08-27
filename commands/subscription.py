from loader import *
from aiogram.types import Message, ContentTypes
from phrases import phrases as P
from states.states import USER
from buttons.buttons import setActionFor, Buttons
from utils import utils
from notifications import to_admin

@setActionFor(USER.SUBSCRIPTION.INFO)
async def subscription_info(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    sub_data = db.fetchone('SELECT subscription, subscription_end FROM users WHERE cid = ?;', (cid,))

    sub_end = utils.str2dt(sub_data[1])
    days_left = (sub_end - utils.now()).days

    markup = Buttons(True)
    markup.add(P.pay_button(cid), USER.SUBSCRIPTION.PAY_INFO)

    if sub_data[0] == -1:
        await chat.edit(P.sub_info_deactivated(cid), markup)
    if sub_data[0] == 0:
        await chat.edit(P.sub_info_free(cid, days_left), markup)
    elif sub_data[0] == 1:
        await chat.edit(P.sub_info_premium(cid, days_left), markup)

    await chat.setState(USER.SUBSCRIPTION.INFO)
    

@setActionFor(USER.SUBSCRIPTION.PAY_INFO)
async def payment_info(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]

    await chat.edit(P.payment_info(cid), Buttons(True))

    await chat.setState(USER.SUBSCRIPTION.PAY_INFO)


@setActionFor(USER.SUBSCRIPTION.INVOICE)
async def invoice(message: Message):
    cid, chat = message.chat.id,cm[message.chat.id]
    
    if message.content_type not in ContentTypes.PHOTO:
        await chat.send(P.wrong_format(cid), temporary=True)
        return

    markup = Buttons()
    markup.add(P.menu(cid), USER.MAIN_MENU)

    await to_admin.invoice(cid, message.photo[0].file_id)
    await chat.edit(P.payment_image_sent(cid), markup)

    await chat.setState(USER.SUBSCRIPTION.INVOICE)
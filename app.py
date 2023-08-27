import asyncio
import logging
import traceback
import signal
import sys

import config
from aiogram import executor
from aiogram.dispatcher.middlewares import BaseMiddleware
from commands import *
from loader import *
from tasks import Tasks
from utils.logging import LoggingMiddleware
from notifications import to_admin

dp.middleware.setup(LoggingMiddleware())

class EnvironmentMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
    async def on_pre_process_update(self, update: types.Update, data: dict):
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
        chat = cm[message.chat.id]
        await chat.pre_process_update(update)


    async def on_post_process_update(self, update: types.Update, result, data: dict):
        if update.callback_query:
            message = update.callback_query.message
        elif update.message:
            message = update.message
        else:
            return 
        chat = cm[message.chat.id]
        chat.post_process_update(update)

dp.middleware.setup(EnvironmentMiddleware())

def all_exception_handler(loop, context):
    text = f"Exception occured:\n {context['exception']}"
    
    tb = context.get("traceback")
    if tb is None:
        tb = context["exception"].__traceback__
    tb = str(context['exception'])  + '\n' + "".join(traceback.format_tb(tb))

    logging.error(tb)
    asyncio.create_task(bot.send_message(config.REPORT_CHANNEL_ID, text=text))

async def on_polling_startup(dp):
    Tasks()
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    handler = logging.FileHandler('botlog.log', 'a', 'utf-8')

    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    root_logger.handlers[0] = handler
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(all_exception_handler)

async def on_polling_shutdown(dp):
    logging.warning("Shutting down..")
    await to_admin.report()
    cm.save_all()
    logging.warning("Bot down")

def signal_handler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    executor.start_polling(dp, on_startup=on_polling_startup,on_shutdown=on_polling_shutdown, skip_updates=False)



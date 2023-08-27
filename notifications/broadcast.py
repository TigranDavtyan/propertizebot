import asyncio
import logging

from loader import *
from aiogram.utils import exceptions, executor
log = logging.getLogger()

def get_users():
    return [u[0] for u in db.fetchall('SELECT cid FROM users ORDER BY account_state ASC;')]


async def forward_message(user_id: int, from_chat: int, message_id: int, disable_notification: bool = False) -> int:
    """
    Safe messages sender

    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.forward_message(user_id, from_chat, message_id, disable_notification=disable_notification) 
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
        db.query('UPDATE users SET account_state=1 WHERE cid=?', (user_id,))
        return 1
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
        db.query('UPDATE users SET account_state=2 WHERE cid=?', (user_id,))
        return 2
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout/2)
        return await forward_message(user_id, from_chat, message_id, disable_notification=disable_notification)   # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
        db.query('UPDATE users SET account_state=3 WHERE cid=?', (user_id,))
        return 3
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
        db.query('UPDATE users SET account_state=0 WHERE cid=?', (user_id,))
        return 4
    else:
        log.info(f"Target [ID:{user_id}]: success")
        db.query('UPDATE users SET account_state=0 WHERE cid=?', (user_id,))
        return 0

async def broadcast_users(from_chat: int, message_id: int, disable_notification) -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """
    results = {0:0, 1:0, 2:0, 3:0, 4:0}

    for user_id in set(get_users()):
        res = 4
        retry = 3
        while retry > 0 and res == 4:
            res = await forward_message(user_id, from_chat, message_id, disable_notification)
            await asyncio.sleep(.15)  # 20 messages per second (Limit: 30 messages per second)

        results[res] += 1

    return results
import asyncio
import datetime
import logging
import random

from config import NIGHT_HOURS, ADMIN_CHAT_ID
from loader import *
from notifications import to_admin, to_users
from utils import utils
from listam import User as LUser

logger = logging.getLogger()

def isNighttime(time: datetime.time) -> bool:
    return time.hour >= NIGHT_HOURS['start'] or time.hour < NIGHT_HOURS['end']

def getRandomNotifyTimeInTheMorning() -> datetime.time:
    return (datetime.datetime(2023,2,12 ,hour = NIGHT_HOURS['end'], minute=0, second=0) + datetime.timedelta(seconds=random.randint(60,600))).time()

class Timers:
    #Wrappers for loops
    #TODO dont like this function
    def run_everyday_at(time: datetime.time):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                now = utils.now()
                next_run = now.replace(hour=time.hour, minute=time.minute, second=time.second)
                if next_run < now:
                    next_run+= datetime.timedelta(days=1)
                wait_time = (next_run - now).total_seconds()-1

                while True:
                    await asyncio.sleep(wait_time)
                    logging.info(f'Running task {function.__name__}')

                    await function(*args, **kwargs)
                    
                    now = utils.now()
                    next_run += datetime.timedelta(days=1)
                    wait_time = (next_run - now).total_seconds()
            return wrapper
        return decorator

    def run_every_round_hour():
        def decorator(function):
            async def wrapper(*args, **kwargs):
                now = utils.now()
                next_run = now.replace(hour=now.hour, minute=0, second=0)
                if next_run < now:
                    next_run += datetime.timedelta(hours=1)
                wait_time = (next_run - now).total_seconds()-1

                while True:
                    await asyncio.sleep(wait_time)
                    logging.info(f'Running task {function.__name__}')

                    await function(*args, **kwargs)
                    
                    now = utils.now()
                    next_run += datetime.timedelta(hours=1)
                    wait_time = (next_run - now).total_seconds()
            return wrapper
        return decorator

    def run_every(seconds):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                while True:
                    logging.info(f'Running task {function.__name__}')
                    await function(*args, **kwargs)
                    
                    await asyncio.sleep(seconds)
            return wrapper
        return decorator

    def run_every_at_day(seconds):
        def decorator(function):
            async def wrapper(*args, **kwargs):
                while True:
                    if not isNighttime(datetime.datetime.now().time()):
                        logging.info(f'Running task {function.__name__}')
                        await function(*args, **kwargs)
                    
                    await asyncio.sleep(seconds)
            return wrapper
        return decorator

    #One time tasks
    async def run_in(seconds: int, func, *args, **kwargs):
        await asyncio.sleep(seconds)
        return await func(*args, **kwargs)
    
    async def run_at(time: datetime.time, func, *args, **kwargs):
        now = utils.now()
        next_run = now.replace(hour=time.hour, minute=time.minute, second=time.second,microsecond=time.microsecond)
        if next_run < now:
            next_run+= datetime.timedelta(days=1)
        wait_time = (next_run - now).total_seconds()
        await asyncio.sleep(wait_time)
        return await func(*args, **kwargs)

class Tasks:
    def __init__(self):
        asyncio.create_task(self.report_activity())
        asyncio.create_task(self.save_old_chats())
        asyncio.create_task(self.check_user_subscriptions())

        asyncio.create_task(self.renewAll1())
        asyncio.create_task(self.renewAll2())

    @Timers.run_every_at_day(3600*24)
    async def report_activity(self):
        await to_admin.report()

    @Timers.run_every_at_day(600)
    async def save_old_chats(self):
        cm.save_old_chats()

    @Timers.run_everyday_at(datetime.time(hour=12, minute=0, second=0))
    async def check_user_subscriptions(self):
        ended_users = db.query("SELECT cid FROM users WHERE subscription > -1 AND subscription_end < DATETIME('now')")
        if not ended_users:
            return
        
        db.query("UPDATE users SET subscription = -1 WHERE subscription > -1 AND subscription_end < DATETIME('now')")

        for cid in ended_users:
            await to_users.subscription_ended(cid)
    
    async def renewAll(self):
        userids = [u[0] for u in db.fetchall('SELECT cid FROM users WHERE subscription > -1;')]
        for cid in userids:
            user = LUser(cid)
            await user.renewListings()

    @Timers.run_everyday_at(datetime.time(hour=9, minute=0, second=0))
    async def renewAll1(self):
        await self.renewAll()

    @Timers.run_everyday_at(datetime.time(hour=16, minute=0, second=0))
    async def renewAll2(self):
        await self.renewAll()
import sys
sys.path.append('../bot/')

from loader import *
from aiogram.types import Message
from phrases import phrases as P
import logging
from utils import utils
import config
from utils import logging as lgm
from buttons.buttons import Buttons
from states.states import ADMIN

async def new_user(message: Message):
        text = f"""New user {message.from_user.full_name}
ID - {message.chat.id}
Username - {message.from_user.username}
Language - {message.from_user.language_code}"""
        
        photos = await message.from_user.get_profile_photos()
        
        if photos.total_count > 0:
            try:
                await cm[config.REPORT_CHANNEL_ID].send(text,photo=photos.photos[0][0].file_id, temporary=True)
            except Exception as e:
                print(e)
                await cm[config.REPORT_CHANNEL_ID].send(text, temporary=True)
        else:
            await cm[config.REPORT_CHANNEL_ID].send(text, temporary=True)
        logging.info(f'NOTIF: ADMIN - {config.REPORT_CHANNEL_ID} new user {message.chat.id}')

async def report():
    all_user_count = db.fetchone('SELECT count(*) FROM users;')[0]
    text = f"Report for the last 1 hour\n<pre>User count - {all_user_count}\n"
    now = utils.now()
    new_users_count = 0
    count = 0
    activity_count = 0
    
    more_than_limit = False
    for userid, activity in lgm.user_activity.items():
        count += 1
        user = db.fetchone('SELECT name, joining_date FROM users WHERE cid = ?', (userid,))

        hours = round((now - utils.str2dt(user[1])).total_seconds() / 3600)
        if now - utils.str2dt(user[1]) < utils.datetime.timedelta(hours=1):
            new_users_count += 1

        activity_count += activity['sent']
        
        if len(text) < 1000:
            text += f"{hours:<3}-{userid:<11}:{user[0][:8]:<8} - {activity['sent']:<3}\n"
        else:
            more_than_limit = True
    
    if more_than_limit:
        text += '......'

    if count > 0:
        text += f"""\nAll users {count} | New users {new_users_count} | {new_users_count/count*100:.1f}% 
Activity All actions {activity_count} | Average {activity_count/count:.1f} actions"""
    text+='</pre>'
    await cm[config.REPORT_CHANNEL_ID].send(text, disable_notification=True)
    lgm.user_activity = {}


async def invoice(user_id, photo_id):
    name, email = db.fetchone('SELECT name, email FROM users WHERE cid = ?', (user_id,))

    markup = Buttons()
    markup.add('Decline', ADMIN.DECLINE_PAYMENT, user_id)
    markup.add('Approve payment for 6 months', ADMIN.ADD_6MONTHS, user_id)
    markup.add('Approve payment for 12 months', ADMIN.ADD_12MONTHS, user_id)

    text = f'User {user_id}:{name}({email}) wants to prolonge the subscription'
    await cm[config.ADMIN_CHAT_ID].send(text, markup, photo_id, temporary=False)
    logging.info(f'NOTIF: ADMIN - {config.ADMIN_CHAT_ID} master {user_id} sent payment check')
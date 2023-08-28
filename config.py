import os
import time
import platform

if platform.system() in ['Linux', 'Darwin']:
    print('Running production mode on Propertize')
    # Set the TZ environment variable
    os.environ['TZ'] = 'Asia/Yerevan'

    # Update the time zone information
    time.tzset()

    TOKEN = '6109475663:AAFoAtl6ykt5uI0j2a82jr0tMaWWPPLZ_d4'

    BOT_USERNAME = 'PropertizeBot'
    REPORT_CHANNEL_ID = -1001919616154
else:
    print('Development mode on davtyantestbot')
    TOKEN = '5986440556:AAG7lYBgZWX8f2ZKS0wauyrAhWq9VqRZYwI'
    
    BOT_USERNAME = 'davtyantestbot'
    REPORT_CHANNEL_ID = -1001830553096

PROJECT_NAME = "Propertize"

DB_PATH = 'data/bot.db'

AMD2USD = 0
AMD2RUB = 0

ADMIN_CHAT_ID = 1710831153 #Tigran Davtyan
# ADMIN_CHAT_ID = 1859746511#Motor Mentor Admin

DEFAULT_LANGUAGE = 0 #Armenian

NIGHT_HOURS = {'start':23,'end': 10}

SUBSCRIPTION_DAYS = 30
BONUS_REFS = 5
BONUS_DAYS_FOR_REFS = SUBSCRIPTION_DAYS

FREE_TRIAL_DAYS = 7
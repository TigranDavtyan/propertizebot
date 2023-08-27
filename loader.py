from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.storage import DatabaseManager
from config import TOKEN
from chat_manager import ChatManager

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
cm = ChatManager(bot)
db = DatabaseManager()
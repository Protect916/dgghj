import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

API_TOKEN = '1678385737:AAHe9sHZp6K_F0TeWUxgu5rwVleH8NfP_YE'

bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler()
async def cmd1_start(message: types.Message):
  await bot.send_message(message.chat.id, 'TEST')
  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

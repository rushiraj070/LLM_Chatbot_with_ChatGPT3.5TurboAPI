import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN = os.getenv('Telegram_TOKEN')
print(API_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or 'help' command
    """

    await message.reply("Hello, Welcome to your own personal space at Rushiraj's Ecosystem.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_uodates=True)
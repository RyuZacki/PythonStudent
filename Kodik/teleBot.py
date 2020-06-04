import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Эхо
@dp.message_handler()
async def echo(message: types.Message):  # <-- разобрать async
    await message.answer(message.text) # <-- разобрать await

# Запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
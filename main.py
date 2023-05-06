from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='TOKEN_HERE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне что-нибудь!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

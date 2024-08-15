import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token="7109887404:AAH5bu59XLjMG1B-eZytIwdouUUa3VYNG_Q")
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
       asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")


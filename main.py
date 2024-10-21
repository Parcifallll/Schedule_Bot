import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router



async def main():
    bot = Bot(token="7739545969:AAEldnloIi7TWDmDy78ADsKGp5586Ckcm_Y")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот оффнут")
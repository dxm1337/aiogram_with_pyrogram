import asyncio
import logging 

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command
from pyrogram import Client

import config
from bot.create_bot import dp, bot


logger = logging.getLogger(__name__)
dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode="HTML")

#If create an instance in this way, there will be an error
app_pyr = Client('newacc',
            api_id=config.ID,
            api_hash=config.HASH,
            phone_number=config.PHONE_NUMBER)

#And it's like norm
def create_pyr():
    return Client('newacc',
            api_id=config.ID,
            api_hash=config.HASH,
            phone_number=config.PHONE_NUMBER)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    @dp.message(Command(commands=["start"]))
    async def command_start_handler(message: Message) -> None:

        #throws an error
        # await app_pyr.start()
        # async for message in app_pyrogram.get_chat_history("me"):
        #     print(message.text)
        # await app_pyr.stop()

        #It's OK
        app_pyrogram = create_pyr()
        await app_pyrogram.start()
        async for message in app_pyrogram.get_chat_history("me"):
            print(message.text)
        await app_pyrogram.stop()

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")

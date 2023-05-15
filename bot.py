import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.user import user_router
from tgbot.handlers.deposit_detail import deposit_detail_router
from tgbot.handlers.transaction_history import transaction_history_router
from tgbot.handlers.main_screen import main_screen_router
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.db import start_db
from tgbot.services import broadcaster

logger = logging.getLogger(__name__)


# async def on_startup(bot: Bot, admin_ids: list[int]):
#     await broadcaster.broadcast(bot, admin_ids, "Бот був запущений")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    await start_db.postgre_start()
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    for router in [
        admin_router,
        user_router,
        deposit_detail_router,
        main_screen_router,
        transaction_history_router,
    ]:
        dp.include_router(router)

    register_global_middlewares(dp, config)

    # await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот був вимкнений!")

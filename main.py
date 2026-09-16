import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, LOG_LEVEL
from database import init_db
from handlers import commands, messages

# Setup logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    """Set bot commands"""
    commands_list = [
        BotCommand(command="start", description="Botni boshlash"),
        BotCommand(command="help", description="Yordam olish"),
        BotCommand(command="me", description="Profil ma'lumotlarim"),
        BotCommand(command="clear", description="Suhbatni o'chirish"),
        BotCommand(command="status", description="Bot holati"),
    ]
    await bot.set_my_commands(commands_list)


async def main():
    """Main function"""
    logger.info("Bot ishga tushmoqda...")
    
    # Initialize database
    await init_db()
    logger.info("Database initialized")
    
    # Initialize bot and dispatcher
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Register routers
    dp.include_router(commands.router)
    dp.include_router(messages.router)
    
    # Set bot commands
    await set_commands(bot)
    
    try:
        # Start polling
        logger.info("Polling boshlandi...")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        logger.info("Bot to'xtatildi")


if __name__ == "__main__":
    asyncio.run(main())

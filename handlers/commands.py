from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import User as TelegramUser

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """Handle /start command"""
    await message.answer(
        f"Assalamu alaikum, {message.from_user.first_name}! 👋\n\n"
        "Men GitHub Copilot bilan ishlash uchun yaratilgan bot-man.\n\n"
        "/help - yordam olish\n"
        "/me - profil ma'lumotlari\n"
    )


@router.message(Command("help"))
async def help_handler(message: types.Message):
    """Handle /help command"""
    help_text = (
        "📚 Yordam:\n\n"
        "/start - Botni qayta boshlash\n"
        "/me - Profil ma'lumotlarim\n"
        "/clear - Suhbatni o'chirish\n"
        "/status - Bot holati\n\n"
        "Shunchaki matn yuboring va men sizga javob beraman! 💬"
    )
    await message.answer(help_text)


@router.message(Command("me"))
async def me_handler(message: types.Message):
    """Handle /me command"""
    user = message.from_user
    profile_text = (
        f"👤 Profil ma'lumotlarim:\n\n"
        f"ID: {user.id}\n"
        f"Ism: {user.first_name}\n"
        f"Familya: {user.last_name or 'Yo\'q'}\n"
        f"Username: @{user.username or 'Yo\'q'}\n"
        f"Til: {user.language_code or 'Noma\'lum'}"
    )
    await message.answer(profile_text)


@router.message(Command("status"))
async def status_handler(message: types.Message):
    """Handle /status command"""
    await message.answer("✅ Bot faol va ishlayotgan holatda!")


@router.message(Command("clear"))
async def clear_handler(message: types.Message):
    """Handle /clear command"""
    await message.answer("🧹 Suhbat tarixi o'chirildi!")

from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

router = Router()


@router.message()
async def echo_handler(message: types.Message):
    """Handle regular messages"""
    try:
        # Echo user message
        await message.answer(
            f"📨 Sizning xabaringiz:\n\n`{message.text}`",
            parse_mode="Markdown"
        )
        
        # TODO: Add GitHub Copilot integration here
        # response = await get_copilot_response(message.text)
        # await message.answer(response)
        
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {str(e)}")

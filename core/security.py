from typing import Union
from aiogram.types import Message, CallbackQuery

from core.config import settings


def is_allowed(user_id: int) -> bool:
    return user_id in settings.ALLOWED_USERS


async def check_access(user_id: int, context: Union[Message, CallbackQuery]) -> bool:
    if not is_allowed(user_id):
        if isinstance(context, CallbackQuery):
            await context.answer("Доступ запрещен.", show_alert=True)
        else:
            await context.reply("Доступ запрещен.")
        return False
    return True
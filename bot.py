import asyncio
import logging
import sys
from os import getenv

from main import cell_value, cell_clear

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery



from keyboards import keyboard_inline


from aiogram import F

TOKEN = getenv('BOT_TOKEN')


dp = Dispatcher()



@dp.message(CommandStart())
async def process_start_command(message: Message) -> None:       
    await message.reply(f"Привет, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard_inline)    



@dp.callback_query(F.data == "500")
async def send_random_value(callback: CallbackQuery):
    value = cell_value(500)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "800")
async def send_random_value(callback: CallbackQuery):
    value = cell_value(800)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "другое")
async def send_random_value(callback: CallbackQuery):
    
    await callback.answer(
        text='ололо',
        show_alert=True
    )


@dp.callback_query(F.data == "очистить")
async def send_random_value(callback: CallbackQuery):
    value = cell_clear()
    await callback.answer(
        text=str(value),
        show_alert=True
    )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

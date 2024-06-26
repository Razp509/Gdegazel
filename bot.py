import asyncio
import logging
import sys
import os

from main import into_cell, cell_clear, all_work_day, all_work_money, work_day, work_money

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message, CallbackQuery


from keyboards.keyboards import keyboard_inline


from aiogram import F

 
TOKEN = os.environ.get('BOT_TOKEN')


dp = Dispatcher()



@dp.message(CommandStart())
async def process_start_command(message: Message) -> None:       
    await message.reply(f"Привет, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard_inline) 


@dp.callback_query(F.data == "500")
async def send_random_value(callback: CallbackQuery):
    value = into_cell(500)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "800")
async def send_random_value(callback: CallbackQuery):
    value = into_cell(800)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "другое")
async def send_random_value(callback: CallbackQuery):    
    await callback.message.answer(
        text='Введите сумму:'
    )
    @dp.message(F.text)
    async def extract_data(message: Message):
        diferent_sum = message.text
        value = into_cell(diferent_sum)
        await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "очистить")
async def send_random_value(callback: CallbackQuery):
    value = cell_clear()
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "info")
async def any_message(callback: CallbackQuery):
    a_w_day, a_w_money, w_day, w_money = all_work_day(), all_work_money(), work_day(), work_money()
    await callback.message.answer(
        f"Всего дней отработанно: {a_w_day}, в этом месяце: {w_day}\n"
        f"Общая сумма заработка: {a_w_money}, в этом месяце: {w_money}"
    )
    await callback.answer()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
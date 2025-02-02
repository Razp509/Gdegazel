import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from core.config import settings
from core.security import check_access
from services.worksheets import into_cell, cell_clear, all_work_day, all_work_money, work_day, work_money
from state.states import Form
from keyboards.keyboards import keyboard_inline

 
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message) -> None:
    if not await check_access(message.from_user.id, message):
        return

    await message.reply(
        f"Привет, {html.bold(message.from_user.full_name)}!\n\n"
        f"Дополнительные ссылки:\n"
        f"- {html.link('Трекер - gdegazel.ru', settings.TRACKER_LINK)}\n\n"
        f"- {html.link('Таблица: Газель - переводы', settings.TABLE_LINK_GAZ_TRANSFER)}\n"
        f"- {html.link('Таблица: Газель - общее', settings.TABLE_LINK_GAZ_TOTAL)}\n"
        f"- {html.link('Таблица: Daihatsu - общее', settings.TABLE_LINK_HIJET_TOTAL)}\n"
        f"- {html.link('Таблица: Контакты', settings.CONTACT_LINK)}\n\n"
        f"- {html.link('Google диск ГАЛИЛЕО', settings.G_DISK)}",
        reply_markup=keyboard_inline,
        parse_mode=ParseMode.HTML
    )


@dp.callback_query(F.data == "500")
async def send_500(callback: CallbackQuery):
    if not await check_access(callback.from_user.id, callback):
        return
    
    value = into_cell(500)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "800")
async def send_800(callback: CallbackQuery):
    if not await check_access(callback.from_user.id, callback):
        return

    value = into_cell(800)
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "другое")
async def send_other(callback: CallbackQuery, state: FSMContext):
    if not await check_access(callback.from_user.id, callback):
        return

    await state.set_state(Form.waiting_for_sum)
    await callback.message.answer(
        text='Введите сумму:'
    )


@dp.message(Form.waiting_for_sum, F.text)
async def extract_data(message: Message, state: FSMContext):
    if not await check_access(message.from_user.id, message):
        return

    diferent_sum = message.text
    value = into_cell(diferent_sum)
    await message.answer(
        text=str(value)
    )
    await state.clear()


@dp.callback_query(F.data == "очистить")
async def clear_cell(callback: CallbackQuery):
    if not await check_access(callback.from_user.id, callback):
        return
    
    value = cell_clear()
    await callback.answer(
        text=str(value),
        show_alert=True
    )


@dp.callback_query(F.data == "info")
async def send_info(callback: CallbackQuery):
    if not await check_access(callback.from_user.id, callback):
        return

    a_w_day, a_w_money, w_day, w_money = all_work_day(), all_work_money(), work_day(), work_money()

    await callback.message.answer(
        f"Всего дней отработано: {a_w_day}, в этом месяце: {w_day}\n"
        f"Общая сумма заработка: {a_w_money}, в этом месяце: {w_money}\n\n",
        parse_mode=ParseMode.HTML
    )
    await callback.answer()



async def main() -> None:
    bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button1 = InlineKeyboardButton(text="Внести 500", callback_data="500")
button2 = InlineKeyboardButton(text="Внести 800", callback_data="800")
button3 = InlineKeyboardButton(text="Внести другую сумму", callback_data="другое")
button4 = InlineKeyboardButton(text="Очистить ячейку", callback_data="очистить") 
keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[[button1, button2], [button3], [button4]], resize_keyboard=True, one_time_keyboard=True)
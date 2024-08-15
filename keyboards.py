from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_name

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог заведений')],
                                     [KeyboardButton(text='Как с нами связаться?'),
                                      KeyboardButton(text='Помощь')]],
                           resize_keyboard=True,

                           input_field_placeholder='Выберите пункт меню...')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.kat_cafe, callback_data=f"category_{category.id}"))
    return keyboard.adjust(3).as_markup()


async def name_cafe(category_id):
    all_name_cafe = await get_category_name(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_name_cafe:
        keyboard.add(InlineKeyboardButton(text=item.name_cafe, callback_data=f"item_{item.id}"))
    return keyboard.adjust(3).as_markup()


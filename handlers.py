from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать на сервис по выбору заведения!', reply_markup=kb.main)


@router.message(F.text == 'Каталог заведений')
async def catalog(message: Message):
    await message.answer('Выберите категорию заведений', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите заведение по категории',
                                  reply_markup=await kb.name_cafe(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали заведение')
    await callback.message.answer(f'Название: {item_data.name_cafe}\nОписание: {item_data.description}\nСредний чек: {item_data.med_price}$')


@router.message(F.text == 'Как с нами связаться?')
async def catalog(message: Message):
    await message.answer('Здесь должны быть контакты, но пока их нет) Поэтому начнем сначала)', reply_markup=kb.main)


@router.message(F.text == 'Помощь')
async def catalog(message: Message):
    await message.answer('Я бы и рада помочь, но пока помощь нужна только мне)', reply_markup=kb.main)


@router.message()
async def all_message(message: Message):
    await message.answer("Пока я не понимаю вас, но совсем скоро я смогу ответить на любой ваш вопрос!", reply_markup=kb.main)

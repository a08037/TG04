import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

#Обработчик команды /start с кнопками "Привет" и "Пока"
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}!", reply_markup=kb.menu_keyboard)

@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

#Обработчик команды /links для отображения кнопок с URL-ссылками
@dp.message(Command("links"))
async def show_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.links_keyboard)

#Динамическое изменение клавиатуры при команде /dynamic
@dp.message(Command("dynamic"))
async def dynamic_menu(message: Message):
    await message.answer("Нажмите кнопку, чтобы показать больше опций:", reply_markup=kb.dynamic_keyboard)

@dp.callback_query(F.data == 'show_more')
async def show_more_options(callback: CallbackQuery):
    more_options_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data='option_1')],
        [InlineKeyboardButton(text="Опция 2", callback_data='option_2')]
    ])
    await callback.message.edit_text("Выберите опцию:", reply_markup=more_options_keyboard)

@dp.callback_query(F.data == 'option_1')
async def option_1(callback: CallbackQuery):
    await callback.answer("Вы выбрали Опция 1")
    await callback.message.answer("Вы выбрали: Опция 1")

@dp.callback_query(F.data == 'option_2')
async def option_2(callback: CallbackQuery):
    await callback.answer("Вы выбрали Опция 2")
    await callback.message.answer("Вы выбрали: Опция 2")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

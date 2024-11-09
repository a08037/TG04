from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура с кнопками "Привет" и "Пока"
menu_keyboard = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Кнопки с URL-ссылками
links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://rbc.ru')],
   [InlineKeyboardButton(text="Музыка", url='https://open.spotify.com/')],
   [InlineKeyboardButton(text="Видео", url='https://youtube.com')]
])

# Динамическое изменение клавиатуры
dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]
])

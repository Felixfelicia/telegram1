from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

register = KeyboardButton("Регистрация")
quiz = KeyboardButton("/quiz")
mem = KeyboardButton("/mem")
game = KeyboardButton("/game")

start_markup.add(register, quiz, mem, game)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel = KeyboardButton("Отмена")
cancel_markup.add(cancel)


direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Backend"),
    KeyboardButton("Frontend"),
    KeyboardButton("Android"),
    KeyboardButton("UX/UI"),
    cancel
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Да"),
    KeyboardButton("Редактировать"),
    cancel
)

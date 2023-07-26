from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram import types

menu = [
    [
        types.KeyboardButton(text='Ипотека 🏡', callback_data='ipot'),
        types.KeyboardButton(text='ЖК 🏘'),
        types.KeyboardButton(text='Акции 🛎')
    ],
    [
        types.KeyboardButton(text='Квартиры 📑'),
        types.KeyboardButton(text='О компании ☑️')
    ],
]
menu = types.ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True, input_field_placeholder='Главное меню 📍')
# - - - О боте - - -
obote = [
    [InlineKeyboardButton(text='Связаться с менеджером 👩‍💼', url='https://t.me/@alena_d_s')],
    [InlineKeyboardButton(text='Связаться с ипотечным специалистом 👩‍💼', url='https://t.me/@arthouse_admin')],
    [InlineKeyboardButton(text='Наш сайт 🌐', url='https://kremlin.ru')],
    [InlineKeyboardButton(text='Наш Telegram-канал 🔗', url='https://t.me/@arthousespb')]
]
obote = InlineKeyboardMarkup(inline_keyboard=obote)
# - - - Ипотека - - -
ipo = [
    [types.KeyboardButton(text='Кредитная история 📋')],
    [types.KeyboardButton(text='Программы ипотеки 🗂')],
    [types.KeyboardButton(text='Бесплатное одобрение 🔖')],
    [types.KeyboardButton(text='Ипотечный калькулятор 🖥')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
ipo = types.ReplyKeyboardMarkup(keyboard=ipo, resize_keyboard=True, input_field_placeholder='Ипотека 🏡')
# - - - Меню -> Ипотека -> Кредитная история - - -
ipo_kred = [
    [types.KeyboardButton(text='Проверка кредитной истории 📋')],
    [types.KeyboardButton(text='Для чего её знать и как улучшить ❓')],
    [types.KeyboardButton(text='Вернуться к ипотеке 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
ipo_kred = types.ReplyKeyboardMarkup(keyboard=ipo_kred, resize_keyboard=True, input_field_placeholder='Кредитная история 📋')
#  - - - Меню -> Вернуться к кредитной истории
back_1 = [
    [types.KeyboardButton(text='Вернуться к кредитной истории 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_1 = types.ReplyKeyboardMarkup(keyboard=back_1, resize_keyboard=True, input_field_placeholder='Выберите нужный пункт')
# - - - Меню -> Ипотека -> Программы по ипотеке - - -
prog = [
    [types.KeyboardButton(text='Описание программ 🗞')],
    [types.KeyboardButton(text='Узнать свою программу 📈')],
    [types.KeyboardButton(text='Вернуться к ипотеке 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
prog = types.ReplyKeyboardMarkup(keyboard=prog, resize_keyboard=True, input_field_placeholder='Программы ипотеки 🗂')
# - - - - - - -
back_2 = [
    [types.KeyboardButton(text='Вернуться к программам по ипотеке 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_2 = types.ReplyKeyboardMarkup(keyboard=back_2, resize_keyboard=True, input_field_placeholder='Выберите нужный '
                                                                                                  'пункт')
# - - - Меню -> Ипотека -> Ипотечный калькулятор - - -
back_ipo = [
    [types.KeyboardButton(text='Вернуться к ипотеке 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_ipo = types.ReplyKeyboardMarkup(keyboard=back_ipo, resize_keyboard=True, input_field_placeholder='Выберите '
                                                                                                      'нужный пункт')
# - - - Меню -> ЖК - - -
jk = [
    [types.KeyboardButton(text='Районы 🏙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
jk = types.ReplyKeyboardMarkup(keyboard=jk, resize_keyboard=True, input_field_placeholder='ЖК 🏘')
# - - - Меню -> ЖК -> Районы - - -
jk_1 = [
    [types.KeyboardButton(text='Комфорт+')],
    [types.KeyboardButton(text='Комфорт')],
    [types.KeyboardButton(text='Эконом')],
    [types.KeyboardButton(text='Вернуться к ЖК 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
jk_1 = types.ReplyKeyboardMarkup(keyboard=jk_1, resize_keyboard=True, input_field_placeholder='Районы 🏙')
# - - - Меню -> ЖК -> Назад к Районам - - -
back_3 = [
    [types.KeyboardButton(text='Вернуться к районам 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_3 = types.ReplyKeyboardMarkup(keyboard=back_3, resize_keyboard=True, input_field_placeholder='Выберите нужный '
                                                                                                  'пункт')
# - - - Меню -> Акции - - -
akz = [
    [
        types.KeyboardButton(text='Скидки 🏷️'),
        types.KeyboardButton(text='Акции 👀'),
        types.KeyboardButton(text='Подарки 🎁')
    ],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
akz = types.ReplyKeyboardMarkup(keyboard=akz, resize_keyboard=True, input_field_placeholder='Акции 🛎')
# - - - Меню -> Назад к акциям
back_4 = [
    [types.KeyboardButton(text='Вернуться к акциям 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_4 = types.ReplyKeyboardMarkup(keyboard=back_4, resize_keyboard=True, input_field_placeholder='Выберите нужный '
                                                                                                    'пункт')
# - - - Меню -> Квартиры
kvar = [
    [types.KeyboardButton(text='Стоимость 💸')],
    [types.KeyboardButton(text='Подборка квартир 🗽')],
    [types.KeyboardButton(text='Сделать личную подборку 🔍')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
kvar = types.ReplyKeyboardMarkup(keyboard=kvar, resize_keyboard=True, input_field_placeholder='Квартиры 🏢')
# - - - Меню -> Назад к квартирам
back_5 = [
    [types.KeyboardButton(text='Вернуться к квартирам 🔙')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
back_5 = types.ReplyKeyboardMarkup(keyboard=back_5, resize_keyboard=True, input_field_placeholder='Выберите нужный '
                                                                                                  'пункт')

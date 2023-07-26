from aiogram import types

menu_admin = [
    [
        types.KeyboardButton(text='Ипотека 🏡'),
        types.KeyboardButton(text='ЖК 🏘'),
        types.KeyboardButton(text='Акции 🛎')
    ],
    [
        types.KeyboardButton(text='Квартиры 📑'),
        types.KeyboardButton(text='О компании ☑️')
    ],
    [types.KeyboardButton(text='Админ-панель')]
]
menu_admin = types.ReplyKeyboardMarkup(keyboard=menu_admin, resize_keyboard=True, input_field_placeholder='Меню админа')

admin_panel = [
    [
        types.KeyboardButton(text='Обновить скидки 🏷️'),
        types.KeyboardButton(text='Обновить аккции 👀'),
        types.KeyboardButton(text='Обновить подарки 🎁'),
    ],
    [types.KeyboardButton(text='Создать рассылку')],
    [types.KeyboardButton(text='Вернуться в главное меню ↩️')]
]
admin_panel = types.ReplyKeyboardMarkup(keyboard=admin_panel, resize_keyboard=True, input_field_placeholder='Админ '
                                                                                                            'панель')

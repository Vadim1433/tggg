from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import config
import kb
import kb_admin
import text
import bd

router = Router()


@router.message(Command('start'))
async def start_handler(msg: types.Message):
    await bd.cmd_start_db(msg.from_user.id)
    await msg.answer_sticker('CAACAgIAAxkBAAKQxmS8N8nUhHQEuxjD0MWFUwKbIFvDAALYDwACSPJgSxX7xNp4dGuYLwQ')
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    if msg.from_user.id == config.ADMIN_ID:
        await msg.answer('Вы авторизовались как администратор!', reply_markup=kb_admin.menu_admin)


@router.message(Command('help'))
async def help_handler(msg: types.Message):
    await msg.answer('Чтобы перезапустить бота напишите /start, либо Меню')


# - - - - - - -
@router.message(F.text == "О компании ☑️")
async def obote(msg: Message):
    await msg.answer(text.obote, reply_markup=kb.obote)


# - - - - - - -
@router.message(F.text == "Ипотека 🏡")
async def ipo(msg: Message):
    await msg.answer(text.ipo, reply_markup=kb.ipo)


@router.message(F.text == "Вернуться к ипотеке 🔙")
async def ipo_back(msg: Message):
    await msg.answer(text.ipo, reply_markup=kb.ipo)


@router.message(F.text == "Кредитная история 📋")
async def ipo_kred(msg: Message):
    await msg.answer(text.ipo_kred, reply_markup=kb.ipo_kred)


@router.message(F.text == "Вернуться к кредитной истории 🔙")
async def ipo_kredback(msg: Message):
    await msg.answer(text.ipo_kred, reply_markup=kb.ipo_kred)


@router.message(F.text == "Проверка кредитной истории 📋")
async def ipo_kred1(msg: Message):
    await msg.answer(text.ipo_kred1, reply_markup=kb.back_1)


@router.message(F.text == "Для чего её знать и как улучшить ❓")
async def ipo_kred2(msg: Message):
    await msg.answer(text.ipo_kred2, reply_markup=kb.back_1)


@router.message(F.text == "Программы ипотеки 🗂")
async def ipo_prog(msg: Message):
    await msg.answer(text.ipo_prog, reply_markup=kb.prog)


@router.message(F.text == "Вернуться к программам по ипотеке 🔙")
async def ipo_progback(msg: Message):
    await msg.answer(text.ipo_prog, reply_markup=kb.prog)


@router.message(F.text == "Узнать свою программу 📈")
async def ipo_prog1(msg: Message):
    await msg.answer(text.ipo_prog1, reply_markup=kb.back_2)


@router.message(F.text == "Описание программ 🗞")
async def ipo_prog2(msg: Message):
    await msg.answer(text.ipo_prog2, reply_markup=kb.back_2)


@router.message(F.text == "Бесплатное одобрение 🔖")
async def ipo_free(msg: Message):
    await msg.answer(text.ipo_free, reply_markup=kb.back_ipo)


@router.message(F.text == "Ипотечный калькулятор 🖥")
async def ipo_cal(msg: Message):
    await msg.answer(text.ipo_cal, reply_markup=kb.back_ipo)


# - - - - - -
@router.message(F.text == "ЖК 🏘")
async def jk(msg: Message):
    await msg.answer(text.jk, reply_markup=kb.jk)


@router.message(F.text == "Вернуться к ЖК 🔙")
async def jk1(msg: Message):
    await msg.answer(text.jk, reply_markup=kb.jk)


@router.message(F.text == "Районы 🏙")
async def jk_street(msg: Message):
    await msg.answer(text.jk_1, reply_markup=kb.jk_1)


@router.message(F.text == "Вернуться к районам 🔙")
async def jk_streetback(msg: Message):
    await msg.answer(text.jk_1, reply_markup=kb.jk_1)


@router.message(F.text == "Комфорт+")
async def jk_street1(msg: Message):
    await msg.answer(text.jk_street1, reply_markup=kb.back_3)


@router.message(F.text == "Комфорт")
async def jk_street2(msg: Message):
    await msg.answer(text.jk_street2, reply_markup=kb.back_3)


@router.message(F.text == "Эконом")
async def jk_street3(msg: Message):
    await msg.answer(text.jk_street3, reply_markup=kb.back_3)


# - - - - - -
@router.message(F.text == "Акции 🛎")
async def akz(msg: Message):
    await msg.answer(text.akz, reply_markup=kb.akz)


@router.message(F.text == "Вернуться к акциям 🔙")
async def akz_back(msg: Message):
    await msg.answer(text.akz, reply_markup=kb.akz)


@router.message(F.text == "Скидки 🏷️")
async def akz_1(msg: Message):
    await msg.answer(text.akz_1, reply_markup=kb.back_4)


@router.message(F.text == "Акции 👀")
async def akz_2(msg: Message):
    await msg.answer(text.akz_2, reply_markup=kb.back_4)


@router.message(F.text == "Подарки 🎁")
async def akz_3(msg: Message):
    await msg.answer(text.akz_3, reply_markup=kb.back_4)


# - - - - - -
@router.message(F.text == "Квартиры 📑")
async def kvar(msg: Message):
    await msg.answer(text.kvar, reply_markup=kb.kvar)


@router.message(F.text == "Вернуться к квартирам 🔙")
async def kvar_back(msg: Message):
    await msg.answer(text.kvar, reply_markup=kb.kvar)


@router.message(F.text == "Стоимость 💸")
async def kvar_1(msg: Message):
    await msg.answer(text.kvar_1, reply_markup=kb.back_5)


@router.message(F.text == "Подборка квартир 🗽")
async def kvar_2(msg: Message):
    await msg.answer(text.kvar_2, reply_markup=kb.back_5)


@router.message(F.text == "Сделать личную подборку 🔍")
async def kvar_3(msg: Message):
    await msg.answer(text.kvar_3, reply_markup=kb.back_5)


# @router.message(F.text == "Меню")
@router.message(F.text == "Главное меню")
@router.message(F.text == "Меню")
@router.message(F.text == "Вернуться в главное меню ↩️")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.message(F.text == "Админ-панель")
async def admin(msg: Message):
    if msg.from_user.id == config.ADMIN_ID:
        await msg.answer('Вы вошли в админ-панель', reply_markup=kb_admin.admin_panel)
    else:
        await msg.answer('Я вас не понимаю, чтобы посмотреть список доступных команд напишите /help')


# - - - Не существующая команда - - -
@router.message()
async def answer(msg: Message):
    await msg.answer('Я вас не понимаю, чтобы посмотреть список доступных команд напишите /help')

from re import search
from datetime import date, timedelta
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.keyboards import (main, date_and_day_of_the_week)
from json import load, dump
from app.parser import parser_main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Приветствую, {message.chat.first_name}! Выбери группу:",
                         reply_markup=main)


@router.message(F.text[2:] == "группа")
async def cmd_start(message: Message):
    group = int((search(r'\d', message.text))[0])
    with open("users.json", "r") as file:
        data = load(file)
        data[message.chat.username] = {'group': group, 'week': 0}
    with open("users.json", "w") as file:
        dump(data, file)
    await message.answer(
        f"Выбери дату ({date.today() - timedelta(days=date.today().weekday()) + timedelta(days=data[message.chat.username]['week'] * 7)} - {date.today() - timedelta(days=date.today().weekday()) + timedelta(days=5) + timedelta(days=data[message.chat.username]['week'] * 7)}):",
        reply_markup=date_and_day_of_the_week)


@router.message(F.text == "Поменять группу")
async def cmd_start(message: Message):
    await message.answer("Выбери группу:",
                         reply_markup=main)


@router.message(F.text == "Пред.неделя")
async def cmd_start(message: Message):
    with open("users.json", "r") as file:
        data = load(file)
        data[message.chat.username] = {'group': data[message.chat.username]['group'],
                                       'week': data[message.chat.username]['week'] - 1}
    with open("users.json", "w") as file:
        dump(data, file)
    await message.answer(
        f"Выбери дату ({date.today() - timedelta(days=date.today().weekday()) + timedelta(days=data[message.chat.username]['week'] * 7)} - {date.today() - timedelta(days=date.today().weekday()) + timedelta(days=5) + timedelta(days=data[message.chat.username]['week'] * 7)}):",
        reply_markup=date_and_day_of_the_week)


@router.message(F.text == "След.неделя")
async def cmd_start(message: Message):
    with open("users.json", "r") as file:
        data = load(file)
        data[message.chat.username] = {'group': data[message.chat.username]['group'],
                                       'week': data[message.chat.username]['week'] + 1}
    with open("users.json", "w") as file:
        dump(data, file)
    await message.answer(
        f"Выбери дату ({date.today() - timedelta(days=date.today().weekday()) + timedelta(days=data[message.chat.username]['week'] * 7)} - {date.today() - timedelta(days=date.today().weekday()) + timedelta(days=5) + timedelta(days=data[message.chat.username]['week'] * 7)}):",
        reply_markup=date_and_day_of_the_week)


@router.message(F.text)
async def cmd_start(message: Message):
    if message.text[:2] in ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ"):

        match message.text[:2]:
            case "ПН":
                day_of_the_week = 0
            case "ВТ":
                day_of_the_week = 1
            case "СР":
                day_of_the_week = 2
            case "ЧТ":
                day_of_the_week = 3
            case "ПТ":
                day_of_the_week = 4
            case "СБ":
                day_of_the_week = 5
        with open("users.json", "r") as file:
            data = load(file)
        datee = date.today() - timedelta(days=date.today().weekday()) + timedelta(days=day_of_the_week) + timedelta(
            days=data[message.chat.username]['week'] * 7)
        username = message.chat.username
        parser_main(username, datee)
        parser_list = parser_main(username, datee)
        string = ''
        for el in parser_list:
            string += f'{el['l_num']}. {el['time']} {el['subject']} {el['stype']} {el['location']} \n\n'
        await message.answer(string,
                             reply_markup=date_and_day_of_the_week)
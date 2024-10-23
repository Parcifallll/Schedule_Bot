from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.methods import get_chat
from datetime import date, timedelta

dt = date.today()
start = dt - timedelta(days=dt.weekday())

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="1 группа"),
                                      KeyboardButton(text="2 группа"),
                                      KeyboardButton(text="3 группа")],
                                     [KeyboardButton(text="4 группа"),
                                      KeyboardButton(text="5 группа"),
                                      KeyboardButton(text="6 группа")],
                                     [KeyboardButton(text="7 группа"),
                                      KeyboardButton(text="8 группа"),
                                      KeyboardButton(text="9 группа")]],
                           resize_keyboard=True)

date_and_day_of_the_week = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Пред.неделя"),
                                      KeyboardButton(text=("ПН")),
                                      KeyboardButton(text=("ВТ")),
                                      KeyboardButton(text=("СР"))],
                                     [KeyboardButton(text=("ЧТ")),
                                      KeyboardButton(text=("ПТ")),
                                      KeyboardButton(text=("СБ")),
                                      KeyboardButton(text="След.неделя")],
                                      [KeyboardButton(text="Поменять группу")]],
                           resize_keyboard=True)

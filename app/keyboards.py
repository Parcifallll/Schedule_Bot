from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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
first_group = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Понедельник_1"),
                                      KeyboardButton(text="Вторник_1"),
                                      KeyboardButton(text="Среда_1")],
                                     [KeyboardButton(text="Четверг_1"),
                                      KeyboardButton(text="Пятница_1"),
                                      KeyboardButton(text="Суббота_1")]],
                           resize_keyboard=True)
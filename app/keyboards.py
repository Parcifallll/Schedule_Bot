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
second_group = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Понедельник_2"),
                                      KeyboardButton(text="Вторник_2"),
                                      KeyboardButton(text="Среда_2")],
                                     [KeyboardButton(text="Четверг_2"),
                                      KeyboardButton(text="Пятница_2"),
                                      KeyboardButton(text="Суббота_2")]],
                           resize_keyboard=True)

third_group = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Понедельник_3"),
                                      KeyboardButton(text="Вторник_3"),
                                      KeyboardButton(text="Среда_3")],
                                     [KeyboardButton(text="Четверг_3"),
                                      KeyboardButton(text="Пятница_3"),
                                      KeyboardButton(text="Суббота_3")]],
                           resize_keyboard=True)

fourth_group = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Понедельник_4"),
                                      KeyboardButton(text="Вторник_4"),
                                      KeyboardButton(text="Среда_4")],
                                     [KeyboardButton(text="Четверг_4"),
                                      KeyboardButton(text="Пятница_4"),
                                      KeyboardButton(text="Суббота_4")]],
                           resize_keyboard=True)

fifth_group = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Понедельник_5"),
                                      KeyboardButton(text="Вторник_5"),
                                      KeyboardButton(text="Среда_5")],
                                     [KeyboardButton(text="Четверг_5"),
                                      KeyboardButton(text="Пятница_5"),
                                      KeyboardButton(text="Суббота_5")]],
                           resize_keyboard=True)
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
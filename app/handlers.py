from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from app.keyboards import (main, first_group, second_group,
                           third_group, fourth_group,
                           fifth_group, sixth_group,
                           seventh_group, eighth_group,
                           ninth_group,)
from .schedule import (FIRST_GROUP_MN, FIRST_GROUP_TU,
                        FIRST_GROUP_WD, FIRST_GROUP_TH,
                        FIRST_GROUP_FR, FIRST_GROUP_SD,
                        SECOND_GROUP_MN, SECOND_GROUP_TU,
                        SECOND_GROUP_WD, SECOND_GROUP_TH,
                        SECOND_GROUP_FR, SECOND_GROUP_SD,
                        THIRD_GROUP_MN, THIRD_GROUP_TU,
                        THIRD_GROUP_WD, THIRD_GROUP_TH,
                        THIRD_GROUP_FR, THIRD_GROUP_SD,
                        FOURTH_GROUP_MN, FOURTH_GROUP_TU,
                        FOURTH_GROUP_WD, FOURTH_GROUP_TH,
                        FOURTH_GROUP_FR, FOURTH_GROUP_SD,
                        FIFTH_GROUP_MN, FIFTH_GROUP_TU,
                        FIFTH_GROUP_WD, FIFTH_GROUP_TH,
                        FIFTH_GROUP_FR, FIFTH_GROUP_SD,
                        SIXTH_GROUP_MN, SIXTH_GROUP_TU,
                        SIXTH_GROUP_WD, SIXTH_GROUP_TH,
                        SIXTH_GROUP_FR, SIXTH_GROUP_SD,
                        SEVENTH_GROUP_MN, SEVENTH_GROUP_TU,
                        SEVENTH_GROUP_WD, SEVENTH_GROUP_TH,
                        SEVENTH_GROUP_FR, SEVENTH_GROUP_SD,
                        EIGHTH_GROUP_MN, EIGHTH_GROUP_TU,
                        EIGHTH_GROUP_WD, EIGHTH_GROUP_TH,
                        EIGHTH_GROUP_FR, EIGHTH_GROUP_SD,
                        NINTH_GROUP_MN, NINTH_GROUP_TU,
                        NINTH_GROUP_WD, NINTH_GROUP_TH,
                        NINTH_GROUP_FR, NINTH_GROUP_SD,)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствую, первокурсник! Выбери группу:",
                         reply_markup=main)

@router.message(F.text == "1 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 1 группы",
                         reply_markup=first_group)

@router.message(F.text == "Понедельник_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "2 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 2 группы",
                         reply_markup=second_group)

@router.message(F.text == "Понедельник_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "3 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 3 группы",
                         reply_markup=third_group)

@router.message(F.text == "Понедельник_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_3")
async def cmd_start(message: Message):
    await message.answer(THIRD_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "4 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 4 группы",
                         reply_markup=fourth_group) 

@router.message(F.text == "Понедельник_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_4")
async def cmd_start(message: Message):
    await message.answer(FOURTH_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "5 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 5 группы",
                         reply_markup=fifth_group)

@router.message(F.text == "Понедельник_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_5")
async def cmd_start(message: Message):
    await message.answer(FIFTH_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "6 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 6 группы",
                         reply_markup=sixth_group)

@router.message(F.text == "Понедельник_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_6")
async def cmd_start(message: Message):
    await message.answer(SIXTH_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "7 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 7 группы",
                         reply_markup=seventh_group)

@router.message(F.text == "Понедельник_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_7")
async def cmd_start(message: Message):
    await message.answer(SEVENTH_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "8 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 8 группы",
                         reply_markup=eighth_group)

@router.message(F.text == "Понедельник_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_8")
async def cmd_start(message: Message):
    await message.answer(EIGHTH_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "9 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 9 группы",
                         reply_markup=ninth_group)

@router.message(F.text == "Понедельник_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_9")
async def cmd_start(message: Message):
    await message.answer(NINTH_GROUP_SD,
                         reply_markup=main)
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7486420116:AAEcZ1gDA_B1zYCq0KWQKGoP5TwRJ_PG0XY")
dp = Dispatcher()

responses = {
    "start": "Привет, <b>{}</b>! Это мой бот-резюме",
    "education": "Являюсь студентом 3 курса Колледжа программирования и кибербезопасности РТУ МИРЭА на специальности 09.02.07 Информационные системы и программирование",
    "soft_skills": "Стрессоутойчивый, ответственный, стремлюсь к изучению нового",
    "hard_skills": "Python на базовом уровне; Git; Английский язык B2",
    "work_experience": "Опыт работы отсутствует",
    "contacts": [
        "Телефон: +7-925-731-03-44",
        "Телеграмм: @ekolesn1kov",
        '<a href="https://github.com/ekolesn1kov">GitHub</a>'
    ]
}

async def send_response(message: Message, key: str):
    if isinstance(responses[key], list):
        for response in responses[key]:
            await message.answer(response, parse_mode=ParseMode.HTML)
    else:
        await message.answer(responses[key].format(message.from_user.full_name), parse_mode=ParseMode.HTML)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await send_response(message, "start")

@dp.message(Command("education"))
async def cmd_education(message: Message):
    await send_response(message, "education")

@dp.message(Command("soft_skills"))
async def cmd_softskills(message: Message):
    await send_response(message, "soft_skills")

@dp.message(Command("hard_skills"))
async def cmd_hardskills(message: Message):
    await send_response(message, "hard_skills")

@dp.message(Command("work_experience"))
async def cmd_workexperience(message: Message):
    await send_response(message, "work_experience")

@dp.message(Command("contacts"))
async def cmd_contacts(message: Message):
    await send_response(message, "contacts")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

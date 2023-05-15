from aiogram import Router, Bot, types
from aiogram.filters import Command, Text, StateFilter
from aiogram.types import Message,FSInputFile
from tgbot.config import load_config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F

import time
from datetime import datetime
import requests
import asyncio

from tgbot.services.del_message import delete_message
from tgbot.misc.functions import reg_user, auf
from tgbot.misc.states import deposit_detail_state

from tgbot.keyboards.textBtn import main_menu_button,network_menu_button,wifi_menu_button,battery_menu_button

from tgbot.keyboards.inlineBtn import CastomCallback
# CastomCallback.filter(F.action == "") // callback_query: types.CallbackQuery, callback_data: SellersCallbackFactory, state: FSMContext

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs


user_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

base = psycopg2.connect(
    dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,
)
cur = base.cursor()

# hanldler for commands
@user_router.message(Command("start"))
async def user_start(message: Message):
    user_id = message.from_user.id
    if await auf(user_id):
        pass
    else:
        await reg_user(user_id,message.from_user.username)
    
    btn = main_menu_button()
    await bot.send_message(user_id, "Здравствуйте, выберите интерисующий вас скриншот",reply_markup=btn.as_markup(resize_keyboard=True))
    

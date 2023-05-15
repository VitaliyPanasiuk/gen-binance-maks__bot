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
import os

from tgbot.services.del_message import delete_message
from tgbot.misc.functions import reg_user, auf
from tgbot.misc.states import transaction_history_state
from tgbot.misc.texts import info_of_screens

from tgbot.gen_img.deposit_detail.deposit_detail import generate_deposit
from tgbot.gen_img.main_screen.main_screen import generate_main_screen
from tgbot.gen_img.transaction_history.transaction_history import generate_transaction_history

from tgbot.keyboards.textBtn import main_menu_button,network_menu_button,wifi_menu_button,battery_menu_button

from tgbot.keyboards.inlineBtn import CastomCallback
# CastomCallback.filter(F.action == "") // callback_query: types.CallbackQuery, callback_data: SellersCallbackFactory, state: FSMContext

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs


transaction_history_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

base = psycopg2.connect(
    dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,
)
cur = base.cursor()
    
    
@transaction_history_router.message(Text('Transaction history'))
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    btn = network_menu_button()
    await bot.send_message(user_id, "Выберите состояние сети",reply_markup=btn.as_markup(resize_keyboard=True))
    
    await state.set_state(transaction_history_state.net)
    
@transaction_history_router.message(F.text.in_({'Два деления', 'Три деления','Четыре деления'}), transaction_history_state.net)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    await state.update_data(user_id=str(user_id))
    
    if text == 'Два деления':
        await state.update_data(net='2')
    elif text == 'Три деления':
        await state.update_data(net='3')
    elif text == 'Четыре деления':
        await state.update_data(net='4')
    
    btn = wifi_menu_button()
    await bot.send_message(user_id, "Выберите состояние подключение к wifi",reply_markup=btn.as_markup(resize_keyboard=True))
    
    await state.set_state(transaction_history_state.wifi)
    
@transaction_history_router.message(F.text.in_({'Два деления', 'Три деления','Одно деление'}), transaction_history_state.wifi)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    
    if text == 'Два деления':
        await state.update_data(wifi='2')
    elif text == 'Три деления':
        await state.update_data(wifi='3')
    elif text == 'Одно деление':
        await state.update_data(wifi='1')
        
    btn = battery_menu_button()
    await bot.send_message(user_id, "Выберите заряд батареи",reply_markup=btn.as_markup(resize_keyboard=True))
    
    await state.set_state(transaction_history_state.battery)
    
@transaction_history_router.message(F.text.in_({'10%', '20%','50%','90%'}), transaction_history_state.battery)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    
    if text == '10%':
        await state.update_data(battery='10')
    elif text == '20%':
        await state.update_data(battery='20')
    elif text == '50%':
        await state.update_data(battery='50')
    elif text == '90%':
        await state.update_data(battery='90')
        
    
    await bot.send_message(user_id, 'Введите дату на телефоне (20:49)',reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(transaction_history_state.time)
    
@transaction_history_router.message(F.text, transaction_history_state.time)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    
    await state.update_data(time=text)
        
    await bot.send_message(user_id, info_of_screens['transaction-history'],reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(transaction_history_state.amount)
    
@transaction_history_router.message(F.text, transaction_history_state.amount)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    
    ios_data = await state.get_data()
    try:
        dt = message.text.splitlines()
        
        tr1 = (dt[0],dt[1],dt[2],dt[3])
        tr2 = (dt[4],dt[5],dt[6],dt[7])
        tr3 = (dt[8],dt[9],dt[10],dt[11])
        tr4 = (dt[12],dt[13],dt[14],dt[15])
        data = {
            'time' : ios_data['time'],
            'net' : ios_data['net'],
            'wifi' : ios_data['wifi'],
            'battery' : ios_data['battery'],
            'list_of_transactions' : (tr1,tr2,tr3,tr4),
            'user_id' : user_id,
        }
        generate_transaction_history(data)
        photo = FSInputFile(f'tgbot/gen_img/transaction_history/{data["user_id"]}_output_transaction_history.png')
        btn = main_menu_button()
        await bot.send_photo(user_id, photo,reply_markup=btn.as_markup(resize_keyboard=True))
        os.remove(f'tgbot/gen_img/transaction_history/{data["user_id"]}_output_transaction_history.png')
        
        await state.clear()
    except Exception as e:
        btn = main_menu_button()
        print(f"Problem with data from user")
        print(e)
        await bot.send_message(user_id, "Данные были введены не верно, попробуйте еще раз",reply_markup=btn.as_markup(resize_keyboard=True))
        await state.clear()
    
    

    
    
    
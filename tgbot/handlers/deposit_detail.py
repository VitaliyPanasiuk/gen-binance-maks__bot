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
# from tgbot.misc.functions import reg_user, auf
from tgbot.misc.states import deposit_detail_state
from tgbot.misc.texts import info_of_screens

from tgbot.gen_img.deposit_detail.deposit_detail import generate_deposit

from tgbot.keyboards.textBtn import main_menu_button,network_menu_button,wifi_menu_button,battery_menu_button

from tgbot.keyboards.inlineBtn import CastomCallback
# CastomCallback.filter(F.action == "") // callback_query: types.CallbackQuery, callback_data: SellersCallbackFactory, state: FSMContext

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs


deposit_detail_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

# base = psycopg2.connect(
#     dbname=config.db.database,
#     user=config.db.user,
#     password=config.db.password,
#     host=config.db.host,
# )
# cur = base.cursor()

    
    
@deposit_detail_router.message(Text('Deposit detail'))
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    btn = network_menu_button()
    await bot.send_message(user_id, "Выберите состояние сети",reply_markup=btn.as_markup(resize_keyboard=True))
    
    await state.set_state(deposit_detail_state.net)
    
@deposit_detail_router.message(F.text.in_({'Два деления', 'Три деления','Четыре деления'}), deposit_detail_state.net)
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
    
    await state.set_state(deposit_detail_state.wifi)
    
@deposit_detail_router.message(F.text.in_({'Два деления', 'Три деления','Одно деление'}), deposit_detail_state.wifi)
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
    
    await state.set_state(deposit_detail_state.battery)
    
@deposit_detail_router.message(F.text.in_({'10%', '20%','50%','90%'}), deposit_detail_state.battery)
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
        
    
    await bot.send_message(user_id, info_of_screens['deposit-detail'],reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(deposit_detail_state.amount)
    
@deposit_detail_router.message(F.text, deposit_detail_state.amount)
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    
    ios_data = await state.get_data()
    try:
        dt = message.text.splitlines()
        data = {
            'time' : dt[0],
            'net' : ios_data['net'],
            'wifi' : ios_data['wifi'],
            'battery' : ios_data['battery'],
            'amount' : dt[1],
            'network' : dt[2],
            'address' : dt[3],
            'txid' : dt[4],
            'date' : dt[5],
            'user_id' : user_id,
        }
        generate_deposit(data)
        photo = FSInputFile(f'tgbot/gen_img/deposit_detail/{data["user_id"]}_output_deposit_detail.png')
        btn = main_menu_button()
        await bot.send_photo(user_id, photo,reply_markup=btn.as_markup(resize_keyboard=True))
        os.remove(f'tgbot/gen_img/deposit_detail/{data["user_id"]}_output_deposit_detail.png')
        
        await state.clear()
    except Exception as e:
        btn = main_menu_button()
        print(f"Problem with data from user")
        print(e)
        await bot.send_message(user_id, "Данные были введены не верно, попробуйте еще раз",reply_markup=btn.as_markup(resize_keyboard=True))
        await state.clear()
    
    

    
    
    
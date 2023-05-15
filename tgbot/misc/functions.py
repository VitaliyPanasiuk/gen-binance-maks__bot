from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

import datetime
import asyncio

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode="HTML")



# async def auf(user_id):
#     base = psycopg2.connect(
#         dbname=config.db.database,
#         user=config.db.user,
#         password=config.db.password,
#         host=config.db.host,
#     )
#     cur = base.cursor()

#     cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
#     buyer = cur.fetchall()
#     if len(buyer) > 0:
#         base.commit()
#         cur.close()
#         base.close()
#         return True
#     else:
#         base.commit()
#         cur.close()
#         base.close()    
#         return False
    
# async def reg_user(user_id,username):
#     base = psycopg2.connect(
#         dbname=config.db.database,
#         user=config.db.user,
#         password=config.db.password,
#         host=config.db.host,
#     )
#     cur = base.cursor()
    
#     cur.execute(f"INSERT INTO users VALUES ({user_id},'{username}')")
    
#     base.commit()
#     cur.close()
#     base.close()
    
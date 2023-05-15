from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class deposit_detail_state(StatesGroup):
    time = State()
    net = State()
    wifi = State()
    battery = State()
    amount = State()
    network = State()
    address = State()
    txid = State()
    date = State()
    user_id = State()
    
class main_screen_state(StatesGroup):
    time = State()
    net = State()
    wifi = State()
    battery = State()
    amount = State()
    network = State()
    address = State()
    txid = State()
    date = State()
    user_id = State()
    
class transaction_history_state(StatesGroup):
    time = State()
    net = State()
    wifi = State()
    battery = State()
    amount = State()
    network = State()
    address = State()
    txid = State()
    date = State()
    user_id = State()
    

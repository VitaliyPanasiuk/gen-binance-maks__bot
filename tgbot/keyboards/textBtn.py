from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types


def main_menu_button():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Deposit detail")
    )
    home_buttons.add(
        types.KeyboardButton(text="Transaction history")
    )
    home_buttons.add(
        types.KeyboardButton(text="Main balance")
    )
    home_buttons.adjust(2)
    return home_buttons

def network_menu_button():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Два деления")
    )
    home_buttons.add(
        types.KeyboardButton(text="Три деления")
    )
    home_buttons.add(
        types.KeyboardButton(text="Четыре деления")
    )
    home_buttons.adjust(2)
    return home_buttons

def wifi_menu_button():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Одно деление")
    )
    home_buttons.add(
        types.KeyboardButton(text="Два деления")
    )
    home_buttons.add(
        types.KeyboardButton(text="Три деления")
    )
    home_buttons.adjust(2)
    return home_buttons

def battery_menu_button():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="10%")
    )
    home_buttons.add(
        types.KeyboardButton(text="20%")
    )
    home_buttons.add(
        types.KeyboardButton(text="50%")
    )
    home_buttons.add(
        types.KeyboardButton(text="90%")
    )
    home_buttons.adjust(2)
    return home_buttons

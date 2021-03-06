from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import reset_inline_button
from bot.schemes.categories import CategoryScheme

categories_keyboard = InlineKeyboardMarkup()
categories_keyboard.add(
    InlineKeyboardButton(CommandEnum.ADD_CATEGORY.value, callback_data=CommandEnum.ADD_CATEGORY.value)
)
categories_keyboard.add(
    InlineKeyboardButton(CommandEnum.LIST_CATEGORY.value, callback_data=CommandEnum.LIST_CATEGORY.value)
)
categories_keyboard.add(reset_inline_button)


retrieve_category_keyboard = InlineKeyboardMarkup()
retrieve_category_keyboard.add(
    InlineKeyboardButton(CommandEnum.DEL_CATEGORY.value, callback_data=CommandEnum.DEL_CATEGORY.value)
)
retrieve_category_keyboard.add(
    InlineKeyboardButton(CommandEnum.FILTER_CATEGORY.value, callback_data=CommandEnum.FILTER_CATEGORY.value)
)
retrieve_category_keyboard.add(reset_inline_button)


def create_retrieve_category_keyboard(categories: List[CategoryScheme]) -> InlineKeyboardMarkup:
    category_keyboard = InlineKeyboardMarkup()
    for category in categories:
        category_keyboard.add(
            InlineKeyboardButton(category.category_name, callback_data=f"category_{category.category_name}")
        )

    category_keyboard.add(reset_inline_button)
    return category_keyboard

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.bot import bot, dp
from bot.commands import CommandEnum
from bot.keyboards.auxiliary import main_keyboard


@dp.message_handler(commands=CommandEnum.START.name.lower())
@dp.message_handler(commands=CommandEnum.HELP.name.lower())
async def start_command(message: types.Message) -> None:
    await message.answer("Hello")
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(state="*", commands=[CommandEnum.RESET.name.lower()])
@dp.message_handler(Text(equals="reset", ignore_case=True), state="*")
async def reset_handler_state(message: types.Message, state: FSMContext) -> None:
    await bot.delete_message(message.from_user.id, message.message_id)
    if await state.get_state():
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == CommandEnum.RESET.value_with_slash, state="*")
async def reset_handler_state_callback(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    if await state.get_state():
        await state.finish()


# @dp.message_handler(commands=["test"])
# async def test(message: types.Message) -> None:
# await bot.send_message(message.from_user.id, dir(message))
# await bot.send_message(message.from_user.id, dir(message.from_user))
# print(dir(message.from_user))
# print(message.from_user)
# print(message.from_user.first_name)
# print(message.from_user.last_name)
# print(message.from_user.username)
# await bot.send_message(message.from_user.id, dir(message.from_user.locale))
# await bot.send_message(message.from_user.id, dir(message.from_user.locale.meta_zones))
# await bot.send_message(message.from_user.id, dir(message.from_user.locale.currencies))

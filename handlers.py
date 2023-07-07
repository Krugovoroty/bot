from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from states import Gen
from aiogram.types.callback_query import CallbackQuery
from aiogram import Bot

import kb
import text
import utils
import config


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=types.ReplyKeyboardRemove())
    await msg.answer(text.menu_choise, reply_markup=kb.menu)

@router.callback_query(F.data == "send_post")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.send_post)
    await clbck.message.edit_text(text.gen_send_post)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)

@router.message(Gen.send_post)
async def process_text_message(msg: Message, state: FSMContext):
    user_message = (msg.from_user.id, msg.date, msg.text)
    await state.set_state(None)
    await msg.answer(text.gen_send_post_image_request, reply_markup=kb.image_request)

@router.callback_query(F.data == "send_image")
async def process_image_message(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.send_image)
    await clbck.message.edit_text(text.gen_send_image)

@router.message(Gen.send_image)
async def process_text_message(msg: Message, state: FSMContext):
    image_filename = await utils.get_photo(msg, msg.bot, config.image_dir)


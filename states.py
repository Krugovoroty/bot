from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    send_post = State()
    send_image = State()
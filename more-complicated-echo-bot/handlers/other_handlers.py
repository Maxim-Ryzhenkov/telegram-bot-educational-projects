
from aiogram import Router
from aiogram.types import Message
from ..lexicon.lexicon import LEXICON_RU


# Инициализируем роутер уровня модуля
router = Router()


@router.message()
async def send_echo(message: Message):
    """ React to receiving any message except commands
        "/start" and "/help" and send it to the user's chat.
        Среагировать на получение любого сообщения кроме команд
        "/start" и "/help" и отправить его в чат пользователю.
    """
    try:

        print("Принят апдейт не пойманный ни одним обработчиком!")
        print(message.model_dump_json(indent=4, exclude_none=True))

        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

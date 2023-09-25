
from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from ..lexicon.lexicon import LEXICON_RU


# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """ Respond to the "/help" command.
        Обработать команду "/help". """
    await message.answer(text=LEXICON_RU['/help'])


async def process_start_command(message: Message):
    """ Respond to the "/start" command.
        Обработать команду "/start". """
    await message.answer(text=LEXICON_RU['/start'])


async def send_photo_echo(message: Message):
    """ React when receiving a photo. And send it to the user’s chat.
        Среагировать на получение фотографии. И отправить ее в чат пользователю.
    """
    print("Принята фотография!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_photo(message.photo[0].file_id)


async def send_audio_echo(message: Message):
    """ React when receiving an audio file. And send it to the user’s chat.
        Среагировать на получение аудиофайла. И отправить его в чат пользователю.
    """
    print("Принят аудиофайл")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer_audio(message.audio.file_id)


async def send_voice_echo(message: Message):
    """ React to receiving a voice message. And send it to the user's chat.
        Среагировать на получение голосового сообщения. И отправить его в чат пользователю.
    """
    print("Принято голосовое сообщение!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text="Получена голосовуха от вас. Вот она.")
    await message.reply_voice(message.voice.file_id)


async def send_video_echo(message: Message):
    """ React to receiving a video message. And send it to the user's chat.
        Среагировать на получение видео-сообщения. И отправить его в чат пользователю.
    """
    print("Принято видео!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_video(message.video.file_id)

# Можно добавить хэндлеры для остальных типов медиаконтента.
# await message.answer_sticker(message.sticker.file_id)
# await message.answer_animation(message.animation.file_id)
# Document


async def send_text_echo(message: Message):
    """ React to receiving a text message. And send it to the user's chat.
        Среагировать на получение текстового сообщения. И отправить его в чат пользователю.
    """
    print("Принято текстовое сообщение!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text=message.text)


# Register handlers
# Регистрируем обработчики
router.message.register(process_start_command, Command(commands='start'))
router.message.register(process_help_command, Command(commands='help'))
router.message.register(send_photo_echo, F.foto)
router.message.register(send_audio_echo, F.audio)
router.message.register(send_voice_echo, F.voice)
router.message.register(send_video_echo, F.video)
router.message.register(send_text_echo)

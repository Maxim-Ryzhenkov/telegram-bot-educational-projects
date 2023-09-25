import os
import dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F


dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create bot and dispatcher objects
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    """ Respond to the "/start" command.
        Обработать команду "/start". """
    await message.answer('Привет! Я эхо-бот!\nНапиши мне что-нибудь, а я повторю твое сообщение.')


async def process_help_command(message: Message):
    """ Respond to the "/help" command.
        Обработать команду "/help". """
    await message.answer(
        'Напиши мне что-нибудь.\nВ ответ я пришлю тебе твое сообщение.\n Больше я ничего не умею.'
    )


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


# Этот хэндлер будет срабатывать на отправку боту голосового сообщения
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


# Этот хэндлер будет срабатывать на любые ваши сообщения,
#
async def send_echo(message: Message):
    """ React to receiving any message except commands
        "/start" and "/help" and send it to the user's chat.
        Среагировать на получение любого сообщения кроме команд
        "/start" и "/help" и отправить его в чат пользователю.
    """
    try:
        print("Принят апдейт не пойманный ни одним обработчиком!")
        # Выведет в консоль структуру апдейта.
        # Нужно только для отладки и удовлетворения любопытства.
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


# Register handlers
# Регистрируем обработчики
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.foto)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_text_echo)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)

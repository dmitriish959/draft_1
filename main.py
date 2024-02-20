import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import os

# вкл логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    # Получаю имя пользователя указанное при регистрации
    user = engine.effective_user
    # Приветствие
    update.message.reply_markdown(fr'Привет, {user.mention_markdown()}!', reply_markup=ForceReply(selective=True))


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Я сам себе помочь не могу, а ты еще тут клацаешь!')


def echo(update: Update, context: CallbackContext) -> None:
    # Зеркалим запрос
    update.message.reply_text(update.message.text)


def main() -> None:
    from dotenv import load_dotenv


    # Загрузка переменных из файла .env
    load_dotenv()

    # Получение значения переменной MY_VARIABLE
    token = os.getenv('TOKEN')

    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()



# вооще не в курсах был про пустую строку

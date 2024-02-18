from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


load_dotenv()
my_variable = os.getenv('MY_TOKEN')

app = ApplicationBuilder().token(my_variable).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

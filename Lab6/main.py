from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6799792060:AAHXAjcep_D3h-Jr-Q9FKWw39rhe92e84Og").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
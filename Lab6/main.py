from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

class TelegramBot:
    
    
    def start(self):
        self.app.run_polling()

    def register_hanlder(self, handler : CommandHandler):
        self.app.add_handler(handler)

    def __init__(self, token : str) -> None:
        self.token = token
        self.userData = { }
        self.app = ApplicationBuilder().token(self.token).build()

async def message_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        ["Age", "Favourite colour"],
        ["Number of siblings", "Something else..."],
        ["Done"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=ReplyKeyboardRemove())

def main():

    bot = TelegramBot("6799792060:AAHXAjcep_D3h-Jr-Q9FKWw39rhe92e84Og")

    bot.register_hanlder(CommandHandler("start", start))

    bot.register_hanlder(MessageHandler(filters.TEXT & (~filters.COMMAND), message_reaction))

    bot.start()

if __name__ == "__main__":
    main()
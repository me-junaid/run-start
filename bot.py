import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Visit Store", url='https://t.me/BankthriftBot/store')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Wanna thrift?', reply_markup=reply_markup)

def main():
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

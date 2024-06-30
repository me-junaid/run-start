import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    # Define the button with a URL
    keyboard = [
        [InlineKeyboardButton("Visit Webapp", url='https://t.me/BankthriftBot/store')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    update.message.reply_text('Click the button below to visit our web app:', reply_markup=reply_markup)

def main():
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

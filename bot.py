    from flask import Flask, request
    from telegram import Update, Bot
    from telegram.ext import CommandHandler, Dispatcher, Updater, CallbackContext
    import os
    import threading

    app = Flask(__name__)

    TOKEN = os.getenv('TELEGRAM_TOKEN')
    bot = Bot(token=TOKEN)

    def start(update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Hello! Welcome to the bot.')

    def run_bot():
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))

        updater.start_polling()
        updater.idle()

    @app.route('/')
    def home():
        return 'Bot is running'

    if __name__ == '__main__':
        threading.Thread(target=run_bot).start()
        app.run(host='0.0.0.0', port=5000)

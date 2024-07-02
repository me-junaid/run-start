from telegram.ext import Updater, CommandHandler
import requests
import threading
import time
import os

# Function to handle /start command
def start(update, context):
    update.message.reply_text('Hello! Your bot is running.')

def main():
    # Get the bot token and chat ID from environment variables
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    # Create the Updater and pass it your bot's token
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handler for /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Start keep-alive mechanism in a separate thread
    threading.Thread(target=keep_alive, args=(token, chat_id)).start()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

def keep_alive(token, chat_id):
    while True:
        try:
            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=keep-alive')
            time.sleep(600)  # Sleep for 10 minutes
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Retry after 1 minute in case of error

if __name__ == '__main__':
    main()
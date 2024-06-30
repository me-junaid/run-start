import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Telegram bot handlers
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2')
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")

# Simple HTTP server to keep the web service alive
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Bot is running')

def run_http_server():
    server_address = ('', int(os.environ.get('PORT', 8000)))
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

def main():
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Telegram bot in a separate thread
    threading.Thread(target=updater.start_polling).start()

    # Start the simple HTTP server
    run_http_server()

if __name__ == '__main__':
    main()

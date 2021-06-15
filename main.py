import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from decouple import config
import os
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = config('annaApi')

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def new_member(update, context):
    print(update.message.new_chat_members)
    for member in update.message.new_chat_members:
        if not member.username:
            if not member.first_name:
                if not member.last_name:
                     update.message.reply_text('Bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
                else: 
                     update.message.reply_text(f'{member.last_name}'+ ', bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
            else:
                update.message.reply_text(f'{member.first_name}'+ ', bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
        else:
            if not member.first_name:
                if not member.last_name:
                    update.message.reply_text(f'@{member.username}'+ ', bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
                else:
                    update.message.reply_text(f'{member.last_name}'+f'(@{member.username})'+ ', bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
            else:
                update.message.reply_text(f'{member.first_name}'+' '+f'{member.last_name}'+f'(@{member.username})'+ ', bine ai venit pe grupul Forza Horizon 5 Romania 🇷🇴!')
        


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # welcome the new users

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://anna-bot-v1-welcome.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
import config
from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

def hello(update: Update, context):
    context.bot.send_message (
        chat_id = update.effective_message.chat_id,
        text = update.effective_message.text
    )

def start(update: Update, context):
    user_name = update.effective_user.first_name
    context.bot.send_message (
        chat_id = update.effective_message.chat_id,
        text = f'Привет, {user_name}' 
    )

def main():
    my_update = Updater (
        token = config.TOKEN,
        base_url = config.PROXI,
        use_context = True
    )

    start_handler = CommandHandler('start', start)
    my_handler = MessageHandler(Filters.all, hello)
    
    my_update.dispatcher.add_handler(start_handler)
    my_update.dispatcher.add_handler(my_handler)

    my_update.start_polling()
    my_update.idle()


if __name__ == '__main__':
    main()

    
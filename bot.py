from pprint import pprint

# import config
# from telegram import Update
# from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

# import httplib2
# import googleapiclient.discovery
# import apiclient.discovery
# from oauth2client.service_account import ServiceAccountCredentials
from service_google_api import google_service, spreadsheet_id

# Файл, полученный в Google Developer Console
# CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
# spreadsheet_id = '1jB2NP8RRxv9jnnFFh5TB8DTPgxoSSxoJvLMfzROBjKk'

# def hello(update: Update, context):
#     context.bot.send_message (
#         chat_id = update.effective_message.chat_id,
#         text = update.effective_message.text
#     )


# def start(update: Update, context):
#     user_name = update.effective_user.first_name
#     context.bot.send_message (
#         chat_id = update.effective_message.chat_id,
#         text = f'Привет, {user_name}' 
#     )


def main():
    # my_update = Updater (
    #     token = config.TOKEN,
    #     base_url = config.PROXI,
    #     use_context = True
    # )

    # start_handler = CommandHandler('start', start)
    # my_handler = MessageHandler(Filters.all, hello)
    
    # my_update.dispatcher.add_handler(start_handler)
    # my_update.dispatcher.add_handler(my_handler)

    # my_update.start_polling()
    # my_update.idle()

    # Авторизуемся и получаем service — экземпляр доступа к API
    # credentials = ServiceAccountCredentials.from_json_keyfile_name (
    #     CREDENTIALS_FILE,
    #     ['https://www.googleapis.com/auth/spreadsheets',
    #     'https://www.googleapis.com/auth/drive']
    # )
    # httpAuth = credentials.authorize(httplib2.Http())
    # service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)
    service = google_service()

    # Пример чтения файла
    values = service.spreadsheets().values().get (
        spreadsheetId=spreadsheet_id,
        range='A1:B1',
        majorDimension='COLUMNS'
    ).execute()
    pprint(values)
    

if __name__ == '__main__':
    main()

    
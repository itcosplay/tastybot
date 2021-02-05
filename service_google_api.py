import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

#from service_google_api import google_service, spreadsheet_id

CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1jB2NP8RRxv9jnnFFh5TB8DTPgxoSSxoJvLMfzROBjKk'

def google_service():
    credentials = ServiceAccountCredentials.from_json_keyfile_name (
        CREDENTIALS_FILE,
        [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build (
        'sheets',
        'v4',
        http = httpAuth
    )
    
    return service

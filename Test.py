pip install --upgrade oauth2client
pip install PyOpenSSL
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Spreadsheet example-9d704ead33c7.json.json', scope)
gc = gspread.authorize(credentials)

import gspread
from google.oauth2.service_account import Credentials

# 認証
scopes = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file('GOOGLE_SHEET_CREDENTIALS.json', scopes=scopes)
client = gspread.authorize(creds)

# スプレッドシートIDを書き換えてください
SHEET_ID = 'あなたのシートID'
sheet = client.open_by_key(SHEET_ID).sheet1

# 1行書き込む
sheet.update('A2', 'Hello from GitHub Actions!')

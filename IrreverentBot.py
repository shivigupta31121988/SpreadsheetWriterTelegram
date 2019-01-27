
from __future__ import print_function
import logging
import telegram
import numpy as np

from telegram.error import NetworkError, Unauthorized
from time import sleep
from textblob import TextBlob


import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


#U+1F3F4

token = 'telegram_chatbot_token_here'
update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(token)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    path_to_csv='/Users/shivigupta/Downloads/ChatbotGodown.xlsx'
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message



            quoteSentence=update.message.text
            quote=quoteSentence.split(';')[0]
            author=quoteSentence.split(';')[1]
            category=quoteSentence.split(';')[2]


            WriteToQuoterSheet(quote,author, category)




            update.message.reply_text(' The quote has been added, thank you!')





def WriteToQuoterSheet(quote,author,category):


    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    
    SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    # sample spreadsheet id , present in the google spreadsheet url
    SAMPLE_RANGE_NAME = 'Sheet1!A2:D'
    #column names from where to fetch the data


    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    max_id=len(values)+1
    valuesInput = [[max_id,quote,author,category]]




    body = {
        'values': valuesInput
    }
    range_name = 'Sheet1!A2:D'
    #column names where to write the data
    value_input_option = 'RAW'
    # result = service.spreadsheets().values().update(
    #     spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_name,
    #     valueInputOption=value_input_option, body=body).execute()
    result = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells appended.'.format(result.get('updates').get('updatedCells')))
    # print('{0} cells updated.'.format(result.get('updatedCells')))


if __name__ == '__main__':
    main()

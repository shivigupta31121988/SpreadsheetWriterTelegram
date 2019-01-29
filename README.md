# SpreadsheetWriterTelegram
Using telegram chat bot, writing and reading from a public google spreadsheet. 
Using telgram api and using the help of BotFather , I have been able to create and publish my chatbot on telgram. 
You can follow the steps in the following link to create and launch your own telegram chatbot https://core.telegram.org/bots 


After we manually create a chatbot, using python and install telegram using the pip command, we can listen to the messages sent to our chatbot.

The file IrreverentBot.py contains the python code to read the messages sent to the chatbot. 

Further on, using the google spreadhseet API, we are reading as well as writing (appending new rows) to the spreadsheet so basically we are substituting a sql database with a google spreadsheet.

Please follow the code and documentation of google spreadsheet with python here 
https://developers.google.com/sheets/api/quickstart/python and to write values
https://developers.google.com/sheets/api/guides/values



This is a feeder service and I have designed an android app which uses this spreadsheet to show quotes . Please refer to the play store link: https://play.google.com/store/apps/details?id=hungrybaba.quoter2


Before we start with the google spreadsheet as database, we have to make the spreadhseet public and publish it, or use the OAuth token to fetch the data from the spreadsheet in a client app, an android app in this case.
Follow this link for more details https://support.wix.com/en/article/setting-your-google-spreadsheet-as-public 

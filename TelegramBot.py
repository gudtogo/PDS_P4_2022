# * run this to install the library
# * pip install pyTelegramBotAPI
# * pip install python-dotenv
# * pip install bottle requests
# * pip install firebase-admin
# * pip install pyngrok
import os
import dotenv
from pyngrok import ngrok
from firebase_admin import credentials
from firebaseManage import *
from itsObjects import *
from botManage import *


if __name__ == '__main__':

    dotenv_file = dotenv.find_dotenv()
    # load globals from the .env file
    dotenv.load_dotenv()
    FIREBASE_URL = os.getenv("FIREBASE_URL")
    CERTIFICATE_FILE = os.getenv("CERTIFICATE_FILE")
    startFirebase(FIREBASE_URL, CERTIFICATE_FILE)
    # start the ngrok tunnel and get the URL
    ngrok_url = ngrok.connect(addr=8080, bind_tls=True).public_url
    # The tunnel gets closed when the .py file stops running.
    prGreen(f'[TelegramBot] URL provided by ngrok: {ngrok_url}')
    # set the value of the ngrok url in our .env file.
    os.environ['SERVER_URL'] = ngrok_url
    # write the changes to the .env file
    dotenv.set_key(dotenv_file, "SERVER_URL", os.environ["SERVER_URL"])
    # get values from the .env file
    API_KEY = os.getenv("API_KEY")
    PORT = os.getenv("PORT")
    SERVER_URL = os.getenv("SERVER_URL")
    # start the TelegramBot
    app = TelegramBot(
        BOT_URL=f'https://api.telegram.org/bot{API_KEY}/', API_KEY=API_KEY, SERVER_URL=SERVER_URL)
    app.setTelegramWebhook()
    app.run(host='localhost', port=PORT)

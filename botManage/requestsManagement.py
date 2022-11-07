import os
import requests
import json
import random
from firebaseManage import *
from firebase_admin import db
from itsObjects import *
from bottle import Bottle, run, post, response, request as bottle_request

DEBUGFN = "[requestsManagement]"
numbers = 0


class BotHandlerMixin:
    API_KEY = os.getenv('API_KEY')
    BOT_URL = f'https://api.telegram.org/bot{API_KEY}/'

    def get_message_id(self, data):
        """
        Method to extract chat id from telegram request.

        Parameters
        ----------
            data : `dict`
                    The data sent by the TelegramAPI about the message.

        Returns
        -------
            `Str`
                The chat id from the message.
        """
        chat_id = data['message']['from']['id']
        return chat_id

    def get_groupchat_id(self, data):
        """
        Method to extract chat id from telegram request.

        Parameters
        ----------
            data : `dict`
                    The data sent by the TelegramAPI about the message.

        Returns
        -------
            `Str`
                The chat id from the message.
        """
        chat_id = data['message']['chat']['id']
        return chat_id


    def get_poll_id(self, data):
        """
        Method to extract the poll id from telegram request.

        Parameters
        ----------
            data : `dict`
                    The data sent by the TelegramAPI about the message.

        Returns
        -------
            `Str`
                The poll id from the message.
        """
        poll_id = data['poll']['id']
        return poll_id

    def get_message(self, data):
        """
        Method to extract the message from telegram request.

        Parameters
        ----------
            data : `dict`
                    The data sent by the TelegramAPI about the message.

        Returns
        -------
            `Str`
                The message itself.
        """
        try:
            message_text = [0, data['message']['text']]
        except KeyError:
            results = data['poll']['options']
            message_text = results
            for chosenalt in results:
                if chosenalt['voter_count'] == 1:
                    message_text = [1, chosenalt['text']]
                    break
            else:
                message_text = [1, 'blank']
        return message_text

    def send_message(self, prepared_data):
        """
        Method to send a message to the user.

        Parameters
        ----------
            prepared_data : `dict`
                    should be in JSON format which includes at least `chat_id` and `text`.
        """
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)

    def send_poll(self, prepared_data):
        """
        Method to send a poll message to the user.

        Parameters
        ----------
            prepared_data : `dict`
                    should be in JSON format which includes at least `chat_id` and the poll itself.

        Returns
        -------
            `str`
            the poll id from where the answer comes.
        """
        DEBUGMN = "[send_poll]"
        message_url = self.BOT_URL + 'sendPoll'
        prGreen(DEBUGFN+DEBUGMN+" sending poll...")
        r = requests.post(message_url, json=prepared_data)
        prGreen(DEBUGFN+DEBUGMN +
                f" poll sent under the id: {r.json()['result']['poll']['id']}")
        return r.json()['result']['poll']['id']

attempts = 10
alive = True

class TelegramBot(BotHandlerMixin, Bottle):


    def __init__(self, BOT_URL, API_KEY, SERVER_URL):
        super(TelegramBot, self).__init__()
        self.BOT_URL = BOT_URL
        self.API_KEY = API_KEY
        self.SERVER_URL = SERVER_URL
        self.route('/', callback=self.post_handler, method="POST")

    def setTelegramWebhook(self):
        """
        Method to set the telegram webhook.

        Returns
        -------
        `True` if successful, `False` otherwise.
        """
        DEBUGMN = "[setTelegramWebhook]"
        try:
            r = requests.get(
                f'https://api.telegram.org/bot{self.API_KEY}/setWebHook?url={self.SERVER_URL}')
            prGreen(DEBUGFN+DEBUGMN+f"Seteado el bot con Status code: {r.status_code}")
        except Exception as err:
            prRed()

    def prepare_data_for_text(self, data, msgType='/hint', question='', hint='', chatID=None):
        """
        Method that takes the data and parse it to JSON format for the text message to be sent.

        Parameters
        ----------
            data : `dict`
                    data received from the previous message.
            msgTyp`[Optional]` : `Str`
                    text message type defaults to hint, accepts `newuser` for a new user, `olduser` for a user that already exists, `code` for a codetype question and any other value for an error message.
            question`[Optional]` : `Str`
                    question in case of a code question.

        Returns
        -------
            `dict`
                the data in JSON format as stated in the TelegramAPI documentation.
        """
        if msgType == '/code:':
            answer = question
        elif msgType == '/number':
            answer = "Escribe un numero del 0 al 100 para intentar adivinar el numero que escogi"
        elif msgType == 'newuser':
            answer = f"Cuenta guardada de manera exitosa, este bot posee 1 juego hasta la fecha, escribe /number para intentar adivinar un numero elegido por el bot, tambien puedes usar el comando /stats para ver los resultados historicos de los usuarios que han jugado"
        elif msgType == 'olduser':
            answer = "Tu cuenta ya existe!!!, escribe /number para intentar adivinar un numero elegido por el bot, tambien puedes usar el comando /stats para ver los resultados historicos de los usuarios que han jugado"
        else:
            answer = "Comando desconocido, intenta: '/number' para jugar a adivinar el numero, o '/stats' para ver los scores historicos."
        if chatID != None:
            chat_id = chatID
        else:
            chat_id = self.get_groupchat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }

        return json_data

    def assign_number_game_handler(self, cuser, data, chatid):
        DEBUGMN = "[number_game_handler]"
        global numbers
        if cuser == None:
            not_registered = self.prepare_data_for_text(
                data, '/code:', f'No has comenzado ningun juego!, escribe "/start" para comenzar!')
            self.send_message(not_registered)
            return
        registered = self.prepare_data_for_text(
            data, '/number', "")
        self.send_message(registered)
        numbers = random.randint(0, 100)

    def try_guessing_number_handler(self, data, chatid, gchatid):
        global attempts
        us = retrieveUser(chatid)
        try:
            user_message = int(data[1])
            if user_message > numbers:
                attempts -= 1
                higher_number = self.prepare_data_for_text(
                    data, '/code:', 'Tu numero es mayor que el mio', "", gchatid)
                self.send_message(higher_number)
                if attempts == 0:
                    lost = self.prepare_data_for_text(
                        data, "/code:", "Perdiste, no quedan mas intentos", "", gchatid)
                    self.send_message(lost)
            elif user_message < numbers:
                attempts -= 1
                prCyan(numbers)
                prGreen(data)
                lower_number = self.prepare_data_for_text(
                    data, '/code:', 'Tu numero es mas bajo que el mio', "", gchatid)
                self.send_message(lower_number)
                if attempts == 0:
                    lost = self.prepare_data_for_text(
                        data, "/code:", "Perdiste, no quedan mas intentos", "", gchatid)
                    self.send_message(lost)
            else:
                correct_number = self.prepare_data_for_text(
                    data, '/code:', 'Numero Correcto!, usa el comando /number para jugar otra vez, o usa el comando /stats para ver el score historico', "", gchatid)
                self.send_message(correct_number)
                us.score += 1
                updateUser(chatID=us.chatID, user=us)
                attempts = 0
        except ValueError:
            incorrect_type = self.prepare_data_for_text(
                data, '/code:', 'Tu numero debe ser un numero entero', "", chatid)
            self.send_message(incorrect_type)
        except (TypeError, KeyError):
            no_number = self.prepare_data_for_text(
                data, '/code:', 'No hay numero para adivinar, use el comando /number para partir', "", chatid)
            self.send_message(no_number)

    def show_stats(self, data, chatid):
        users = db.reference('/ID').get()
        text = ""
        for user in users:
            text += "El score de {} es: {}\n".format(users.get(user)['nickname'], users.get(user)['score']) 
            #prGreen("El score de {} es: {}".format(users.get(user)['nickname'], users.get(user)['score']))
        stat_to_message = self.prepare_data_for_text(
            data, '/code:', text, "", chatid)
        self.send_message(stat_to_message)
    def post_handler(self):
        global attempts
        global alive
        """
        Method that handles receiving and sending messages from/to the TelegramAPI.
        """
        DEBUGMN = "[post_handler]"
        data = bottle_request.json
        prGreen(DEBUGFN+DEBUGMN+f" data_received: {data}")
        message_text = self.get_message(data)
        if ('poll' in data):
            self.poll_answer_handler(message_text[1], data)
        else:
            chatid = self.get_message_id(data)
            gchatid = self.get_groupchat_id(data)
            prCyan(chatid)
            prGreen(DEBUGFN+DEBUGMN+" text message received")
            if message_text[1] == '/start':
                prGreen(DEBUGFN+DEBUGMN+" new user request")
                chat_id = data['message']['from']['id']
                user_nickname = data['message']['from']['first_name']
                if detectNewUser(str(chat_id), user_nickname):
                    nuser_data = self.prepare_data_for_text(data, 'newuser')
                else:
                    nuser_data = self.prepare_data_for_text(data, 'olduser')
                self.send_message(nuser_data)
            elif (message_text[1] == '/number'):
                attempts = 10
                cuser = retrieveUser(chatid)
                self.assign_number_game_handler(cuser, data, chatid)
            elif (message_text[1] == '/stats'):
                self.show_stats(data, chatid)
            else:
                if attempts == 0:
                    not_alive = self.prepare_data_for_text(
                        data, '/code:', 'No tienes ningun juego activo, usa el comando /number para empezar uno')
                    self.send_message(not_alive)
                elif attempts >= 1:
                    self.try_guessing_number_handler(message_text, chatid, gchatid)

import os
import requests
import json
import random
from time import sleep
from threading import Thread
from datetime import datetime
from firebaseManage import *
from firebase_admin import db
from itsObjects import *
from bottle import Bottle, run, post, response, request as bottle_request

DEBUGFN = "[requestsManagement]"
numbers = 0
answers = []
correctAnswer2 = 0
poll_group_id = 0

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
        try:
            chat_id = data['message']['from']['id']
        except KeyError:
            return
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
        try:
            chat_id = data['message']['chat']['id']
        except KeyError:
            return
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
        try:
            poll_id = data['poll']['id']
        except KeyError:
            return
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
            try:
                results = data['poll']['options']
                message_text = results
                for chosenalt in results:
                    if chosenalt['voter_count'] == 1:
                        message_text = [1, chosenalt['text']]
                        break
                    else:
                        message_text = [1, 'blank']
            except KeyError:
                return
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
        global answers
        global correctAnswer2
        global poll_group_id
        DEBUGMN = "[send_poll]"
        message_url = self.BOT_URL + 'sendPoll'
        prGreen(DEBUGFN+DEBUGMN+" sending poll...")
        poll_group_id = int(prepared_data['chat_id'])
        prCyan(prepared_data)
        answers = prepared_data['options']
        correct_answer_position = int(prepared_data['correct_option_id'])
        correctAnswer2 = answers[correct_answer_position]
        r = requests.post(message_url, json=prepared_data)
        prCyan(r.json())
        prGreen(DEBUGFN+DEBUGMN +
                f" poll sent under the id: {r.json()['result']['poll']['id']}")
        return r.json()['result']['poll']['id']

    def get_amount_of_chat_members(self, group_chat_id):
        api_call = 'https://api.telegram.org/bot5743843464:AAHztkWYXcVAAjYXQJotEY-AqokUgDIz5hA/getChatMembersCount?chat_id={}'.format(group_chat_id)

        call = requests.post(api_call)

        return int(call.json()['result']) - 1

max_number = 0
position = 0
time = 0
alive = True
activeGame = False
user = 0
auxVar = 0
auxVar2 = 0
number_of_questions = 0
data_for_trivia = 0
number_of_players = 0
participants = 0
player_score = {}
closed_poll = False
activeTime = False
poll_timer = datetime
next_poll = 0

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
        global max_number
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
            answer = "Juego number iniciado!, Escriban un numero del 0 al {} para intentar adivinar el numero que escogi".format(max_number)
        elif msgType == 'newuser':
            answer = f"Cuenta guardada de manera exitosa. \nEste bot posee 3 comandos hasta la fecha: \n/number n_intentos n_max: juego de adivinar un numero elegido por el bot de 0 hasta el numero maximo especificado con un numero de intentos por usuario limitados.\n/trivia first n_preguntas: juego de preguntas de distintos topicos, el usuario que responde primero correctamente gana el puntaje, la cantidad de preguntas que sale es determinado por n_preguntas \n/stats: se muestran las estadisticas de todos los jugadores del grupo"
        elif msgType == 'olduser':
            answer = "Tu cuenta ya existe!!!, escribe (/number n_intentos n_max) para intentar adivinar un numero elegido por el bot, tambien puedes usar el comando /stats para ver los resultados historicos de los usuarios que han jugado"
        else:
            answer = "Comando desconocido, intenta: '(/number n_intentos n_max)' para jugar a adivinar el numero, o '/stats' para ver los scores historicos."

        if chatID != None:
            chat_id = chatID
        else:
            chat_id = self.get_groupchat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }

        return json_data

    def prepare_data_for_poll(self, data, question, position):
        """
        Method that takes the data and parse it to JSON format for the poll to be sent.
        Parameters
        ----------
            data : `dict`
                    data received from the previous message.
            question : `Question`
                    Question to be asked.
        Returns
        -------
            `dict`
                the data in JSON format as stated in the TelegramAPI documentation.
        """
        DEBUGMN = "[prepare_data_for_poll]"
        gchat_id = self.get_groupchat_id(data)
        json_data = {
            "chat_id": gchat_id,
            "question": question[position].question,
            "options": question[position].alternatives,
            "correct_option_id": question[position].answer,
            "type": "quiz",
            "is_anonymous": "False"
        }
        prGreen(DEBUGFN+DEBUGMN+"Data for poll prepared")
        return json_data

    def prepare_data_for_poll2(self, data, question, position, time):
        """
        Method that takes the data and parse it to JSON format for the poll to be sent.
        Parameters
        ----------
            data : `dict`
                    data received from the previous message.
            question : `Question`
                    Question to be asked.
        Returns
        -------
            `dict`
                the data in JSON format as stated in the TelegramAPI documentation.
        """
        DEBUGMN = "[prepare_data_for_poll]"
        gchat_id = self.get_groupchat_id(data)
        json_data = {
            "chat_id": gchat_id,
            "question": question[position].question,
            "options": question[position].alternatives,
            "correct_option_id": question[position].answer,
            "type": "quiz",
            "is_anonymous": "False",
            "open_period": time
        }
        prGreen(DEBUGFN+DEBUGMN+"Data for poll prepared")
        return json_data

    def trivia_first_handler(self, data, gchatid, message):
        DEBUGMN = "[prepare_data_for_poll]"
        success, question = retrieveQuestions()
        global position
        global number_of_questions
        global activeGame
        n_questions = message.split()
        number_of_questions = int(n_questions[2])
        if number_of_questions >= 1:
            if success:
                poll_data = self.prepare_data_for_poll(data, question, position)
                self.send_poll(poll_data)
            else:
                position = 0
                prRed(DEBUGFN+DEBUGMN +
                    " No question found!")
        else:
            invalido = self.prepare_data_for_text(
                            data, '/code:', 'Parametro del comando invalido', "", gchatid)
            self.send_message(invalido)
            activeGame = False

    def trivia_first_handler2(self, data):
        success, question = retrieveQuestions()
        global position
        if success:
            poll_data = self.prepare_data_for_poll(data, question, position)
            self.send_poll(poll_data)

    def poll_answer_handler(self, given_answer, data, user, questions):
        global answers
        global position
        DEBUGMN = "[poll_answer_handler]"
        prGreen(DEBUGFN+DEBUGMN+" poll answer received!")
        correct_answer_position = int(json.dumps(data['poll']['correct_option_id']))
        correct_answer = answers[correct_answer_position]
        prRed(correct_answer)

        if given_answer == correct_answer:
            prCyan(f"Respuecta correcta con respuesta de usuario = {given_answer} y respuesta correcta = {correct_answer}")
        else:
            prRed("Respuesta incorrecta")

    def trivia_time_handler(self, data, gchatid, message):
        DEBUGMN = "[prepare_data_for_poll]"
        success, question = retrieveQuestions()
        global position
        global number_of_questions
        global time
        global next_poll
        global activeGame
        global activeTime
        n_questions = message.split()
        number_of_questions = int(n_questions[2])
        time = int(n_questions[3])
        if ((number_of_questions >= 1) and (time >= 5) and (time <= 599)):
            next_poll = time 
            if success:
                poll_data = self.prepare_data_for_poll2(data, question, position, time)
                self.send_poll(poll_data)
            else:
                position = 0
                prRed(DEBUGFN+DEBUGMN +
                    " No question found!")
        else:
            invalido = self.prepare_data_for_text(
                            data, '/code:', 'Parametro del comando invalido', "", gchatid)
            self.send_message(invalido)
            activeGame = False
            activeTime = False

    def trivia_time_handler2(self, data):
        success, question = retrieveQuestions()
        global position
        global time
        if success:
            poll_data = self.prepare_data_for_poll2(data, question, position, time)
            self.send_poll(poll_data)
    
    def assign_number_game_handler(self, cuser, data, chatid, gchatid, params):
        DEBUGMN = "[number_game_handler]"
        message = params.split()
        global numbers
        global max_number
        global activeGame
        ready = False
        if (int(message[1]) > 0):
            ready = True
        else:
            invalido = self.prepare_data_for_text(
                            data, '/code:', 'Parametro del comando invalido', "", gchatid)
            self.send_message(invalido)
            activeGame = False
        if ready == True:
            attempts = int(message[1])
            max_number = int(message[2])
            prRed(max_number)
            numbers = random.randint(0, max_number)
            registered = self.prepare_data_for_text(
                data, '/number', "")
            self.send_message(registered)
            activeGame = True
            users = db.reference('/ID').get()
            for user in users:
                us = retrieveUser(user)
                us.attempts = attempts
                updateUser(chatID=us.chatID, user=us)


    def try_guessing_number_handler(self, data, chatid, gchatid, user):
        #global attempts
        global activeGame
        global max_number
        us = retrieveUser(chatid)
        try:
            user_message = int(data.split(" ")[1])
            if user_message > max_number or user_message < 0:
                invalid_number = self.prepare_data_for_text(
                    data, '/code:', '{}, {} no pertence al rango valido'.format(user, user_message), "", gchatid)
                self.send_message(invalid_number)
            elif user_message > numbers:
                us.attempts = us.attempts-1
                updateUser(chatID=us.chatID, user=us)
                higher_number = self.prepare_data_for_text(
                    data, '/code:', '{}, {} es mayor que el numero a adivinar'.format(user, user_message), "", gchatid)
                self.send_message(higher_number)
                if us.attempts == 0:
                    lost = self.prepare_data_for_text(
                        data, "/code:", "{} Perdiste, no te quedan mas intentos".format(user), "", gchatid)
                    self.send_message(lost)
            elif user_message < numbers:
                us.attempts = us.attempts-1
                updateUser(chatID=us.chatID, user=us)
                prCyan(numbers)
                prGreen(data)
                lower_number = self.prepare_data_for_text(
                    data, '/code:', '{}, {} es mas bajo que el numero a adivinar'.format(user, user_message), "", gchatid)
                self.send_message(lower_number)
                if us.attempts == 0:
                    lost = self.prepare_data_for_text(
                        data, "/code:", "{} Perdiste, no te quedan mas intentos".format(user), "", gchatid)
                    self.send_message(lost)
            else:
                correct_number = self.prepare_data_for_text(
                    data, '/code:', '{} es el Numero Correcto!, {} adivino el numero y gano 1 punto, usen el comando (/number n_intentos n_max) para jugar otra vez, o usa el comando /stats para ver el score historico'.format(user_message, user), "", gchatid)
                self.send_message(correct_number)
                us.score += 1
                updateUser(chatID=us.chatID, user=us)
                activeGame = False

                users2 = db.reference('/ID').get()
                for user2 in users2:
                    us2 = retrieveUser(user2)
                    us2.attempts = 0
                    updateUser(chatID=us2.chatID, user=us2)

        except ValueError:
            incorrect_type = self.prepare_data_for_text(
                data, '/code:', '{}, Tu numero debe ser un numero entero'.format(user), "", gchatid)
            self.send_message(incorrect_type)
        except (TypeError, KeyError):
            no_number = self.prepare_data_for_text(
                data, '/code:', '{}, No hay numero para adivinar, use el comando /number para partir'.format(user), "", gchatid)
            self.send_message(no_number)

    def show_stats(self, data, gchatid):
        users = db.reference('/ID').get()
        
        scores = []
        users2 = []
        for user in users:
            if (users.get(user)['chatID'].split("|")[1] == str(gchatid)):
                userscore = users.get(user)['score']
                scores.append(userscore)
                users2.append(user)
        scores.sort(reverse=True)

        sorted_users = []
        i = 0
        while(len(sorted_users) != len(users2)):
            for user in users2:
                if(users.get(user)['score'] == scores[i]):
                    sorted_users.append(user)
            i += 1
        
        text = ""
        for user in sorted_users:
            text += "El score de {} es: {}\n".format(users.get(user)['nickname'], users.get(user)['score']) 
            #prGreen("El score de {} es: {}".format(users.get(user)['nickname'], users.get(user)['score']))
        stat_to_message = self.prepare_data_for_text(
            data, '/code:', text, "", gchatid)
        self.send_message(stat_to_message)

    def post_handler(self):
        global alive
        global activeGame
        global user
        global auxVar
        global answers
        global correctAnswer2
        global data_for_trivia
        global number_of_questions
        global position
        global poll_group_id
        global number_of_players
        global participants
        global player_score
        global closed_poll
        global activeTime
        global poll_timer
        global next_poll
        global time
        global auxVar2
        """
        Method that handles receiving and sending messages from/to the TelegramAPI.
        """
        DEBUGMN = "[post_handler]"
        data = bottle_request.json
        prGreen(DEBUGFN+DEBUGMN+f" data_received: {data}")
        prRed(auxVar2)
        prRed(activeTime)
        try:
            if ((auxVar == 1) and (activeTime == False)):
                auxVar = 0

                try:
                    userAnswer = answers[int(data['poll_answer']['option_ids'][0])]
                except KeyError:
                    userAnswer = ""
                    return
                if userAnswer == correctAnswer2 and closed_poll == False:
                    user_answering = data['poll_answer']['user']['first_name'] 
                    gchatid = poll_group_id
                    poll_question_answer = self.prepare_data_for_text(
                            data, '/code:', 'El usario {} respondio correctamente la pregunta anterior!, esperando a que todos los participantes terminen de responder...'.format(user_answering), "", gchatid)
                    self.send_message(poll_question_answer)
                    us2 = retrieveUser(str(data['poll_answer']['user']['id'])+"|"+ str(gchatid))
                    number_of_questions -= 1
                    position += 1
                    player_score[str(us2.chatID)] = player_score[str(us2.chatID)] + 1
                    closed_poll = True

                participants -= 1
                if (participants == 0):
                    if (closed_poll == False):
                        no_correct_answer = self.prepare_data_for_text(
                                data, '/code:', 'Ningun usuario respondio correctamente la pregunta anterior, enviando la siguiente pregunta...', "", poll_group_id)
                        self.send_message(no_correct_answer)
                        number_of_questions -= 1

                    if (number_of_questions == 0):
                        gchatid = poll_group_id
                        winner_id = max(player_score, key=player_score.get)
                        winner_user = retrieveUser(winner_id)
                        winner_user.score += 1
                        updateUser(chatID=winner_user.chatID, user=winner_user)
                        keys = {}
                        for key in player_score:
                            if key != winner_user.chatID:
                                keys[key] = player_score[key]

                        prRed(keys)

                        ended_game = self.prepare_data_for_text(
                            data, '/code:', 'Juego terminado!, el ganador del juego fue {} con {} respuestas correctas. \nEl puntaje de los otros participantes fue:'.format(winner_user.nickname, player_score[winner_user.chatID]), "", gchatid)
                        self.send_message(ended_game)
                        text = ""
                        for key in keys:
                            usss = retrieveUser(key)
                            text += " {} : {} \n".format(usss.nickname ,keys[key])
                            ended_game2 = self.prepare_data_for_text(
                                data, '/code:', text, "", gchatid)
                            self.send_message(ended_game2)
                        position = 0
                        activeGame = False
                        closed_poll = False
                        participants = number_of_players
                        return
                    closed_poll = False
                    self.trivia_first_handler2(data_for_trivia)
                    participants = number_of_players
            elif ((auxVar2 == 1) and (activeTime == True)):
                auxVar2 = 0

                userAnswer = answers[int(data['poll_answer']['option_ids'][0])]
                if userAnswer == correctAnswer2:
                    user_answering = data['poll_answer']['user']['first_name'] 
                    gchatid = poll_group_id
                    #poll_question_answer = self.prepare_data_for_text(
                    #        data, '/code:', 'El usario {} respondio correctamente la pregunta anterior!, esperando a que termine el tiempo...'.format(user_answering), "", gchatid)
                    #self.send_message(poll_question_answer)
                    us2 = retrieveUser(str(data['poll_answer']['user']['id'])+"|"+ str(gchatid))
                    number_of_questions -= 1
                    position += 1
                    tiempo = (datetime.now() - poll_timer).total_seconds()
                    player_score[str(us2.chatID)] = player_score[str(us2.chatID)] + 1*int(tiempo)
                """ 
                #participants -= 1
                if (next_poll == 0):
                    if (closed_poll == False):
                        no_correct_answer = self.prepare_data_for_text(
                                data, '/code:', 'Ningun usuario respondio correctamente la pregunta anterior, enviando la siguiente pregunta...', "", poll_group_id)
                        self.send_message(no_correct_answer)
                        number_of_questions -= 1
                """   
                
                    #participants = number_of_players
                    
                    #self.trivia_time_handler2(data_for_trivia)
                    #participants = number_of_players

            elif ('poll' in data and auxVar == 0 and activeTime == False):
                message_text = self.get_message(data)
                auxVar = 1
                #self.poll_answer_handler(message_text[1], data, user)
            elif ('poll' in data and auxVar2 == 0 and activeTime == True):
                message_text = self.get_message(data)
                auxVar2 = 1
                #self.poll_answer_handler(message_text[1], data, user)
            else:
                message_text = self.get_message(data)
                chatid = self.get_message_id(data)
                gchatid = self.get_groupchat_id(data)
                prGreen(DEBUGFN+DEBUGMN+" text message received")
                user_nickname = data['message']['from']['first_name']
                prCyan(user_nickname)
                if (message_text[1] == '/start'):
                    prGreen(DEBUGFN+DEBUGMN+" new user request")
                    chat_id = data['message']['from']['id']

                    if detectNewUser(str(chat_id) + "|" + str(gchatid), user_nickname):
                        nuser_data = self.prepare_data_for_text(data, 'newuser', "", "", gchatid)
                    else:
                        nuser_data = self.prepare_data_for_text(data, 'olduser', "", "", gchatid)
                    self.send_message(nuser_data)
                elif ('/number' in message_text[1]):
                    cuser = retrieveUser(str(chatid)+ "|" + str(gchatid))
                    if cuser == None:
                        not_registered = self.prepare_data_for_text(
                            data, '/code:', f'Para utilizar el bot debes registrarte, escribe "/start" para comenzar!')
                        self.send_message(not_registered)
                        return
                    if(activeGame == False):
                        prRed(message_text[1])
                        self.assign_number_game_handler(cuser, data, str(chatid)+ "|" + str(gchatid), gchatid, message_text[1])
                    else:
                        not_alive = self.prepare_data_for_text(
                            data, '/code:', '{}, no puedes iniciar otro juego, espera a que el juego activo termine'.format(user_nickname), "", gchatid)
                        self.send_message(not_alive)
                elif (('/trivia' in message_text[1]) and ('first' in message_text[1])):
                    cuser = retrieveUser(str(chatid)+ "|" + str(gchatid))
                    if cuser == None:
                        not_registered = self.prepare_data_for_text(
                            data, '/code:', f'Para utilizar el bot debes registrarte, escribe "/start" para comenzar!')
                        self.send_message(not_registered)
                        return
                    if (activeGame == True):
                        not_alive = self.prepare_data_for_text(
                            data, '/code:', '{}, no puedes iniciar otro juego, espera a que el juego activo termine'.format(user_nickname), "", gchatid)
                        self.send_message(not_alive)
                        return
                    
                    users = db.reference('/ID').get()

                    for user in users:
                        if (users.get(user)['chatID'].split("|")[1] == str(gchatid)):
                            player_score[users.get(user)['chatID']] = 0
    
                    number_of_players = self.get_amount_of_chat_members(gchatid)
                    participants = number_of_players
                    data_for_trivia = data
                    prGreen(DEBUGFN+DEBUGMN+" Starting Trivia First Game")
                    activeGame = True
                    self.trivia_first_handler(data, gchatid, message_text[1])
                    
                elif (('/trivia' in message_text[1]) and ('time' in message_text[1])):
                    cuser = retrieveUser(str(chatid)+ "|" + str(gchatid))
                    if cuser == None:
                        not_registered = self.prepare_data_for_text(
                            data, '/code:', f'Para utilizar el bot debes registrarte, escribe "/start" para comenzar!')
                        self.send_message(not_registered)
                        return
                    if (activeGame == True):
                        not_alive = self.prepare_data_for_text(
                            data, '/code:', '{}, no puedes iniciar otro juego, espera a que el juego activo termine'.format(user_nickname), "", gchatid)
                        self.send_message(not_alive)
                        return

                    users = db.reference('/ID').get()

                    for user in users:
                        if (users.get(user)['chatID'].split("|")[1] == str(gchatid)):
                            player_score[users.get(user)['chatID']] = 0
                    
                    number_of_players = self.get_amount_of_chat_members(gchatid)
                    participants = number_of_players
                    data_for_trivia = data
                    prGreen(DEBUGFN+DEBUGMN+" Starting Trivia Time Game")
                    activeTime = True
                    activeGame = True
                    self.trivia_time_handler(data, gchatid, message_text[1])
                    t1 = Thread(target=self.timer(time))
                    t1.start()
                    poll_timer = datetime.now()
                    prRed(poll_timer)
                    
                elif (message_text[1] == '/stats'):
                    cuser = retrieveUser(str(chatid)+ "|" + str(gchatid))
                    if cuser == None:
                        not_registered = self.prepare_data_for_text(
                            data, '/code:', f'Para utilizar el bot debes registrarte, escribe "/start" para comenzar!')
                        self.send_message(not_registered)
                        return
                    self.show_stats(data, gchatid)
                elif ('/play' in message_text[1]):
                    cuser = retrieveUser(str(chatid)+ "|" + str(gchatid))
                    if cuser == None:
                        not_registered = self.prepare_data_for_text(
                            data, '/code:', f'Para utilizar el bot debes registrarte, escribe "/start" para comenzar!')
                        self.send_message(not_registered)
                        return
                    if activeGame == False:
                        return
                    if ((activeGame == True) and (cuser.attempts == 0)):
                        not_alive = self.prepare_data_for_text(
                            data, '/code:', '{}, ya no tienes mas intentos, espera a que el juego termine'.format(user_nickname), "", gchatid)
                        self.send_message(not_alive)
                    elif ((activeGame == True) and (cuser.attempts >= 1)):
                        self.try_guessing_number_handler(message_text[1], str(chatid)+ "|" + str(gchatid), gchatid, user_nickname)
                else:
                    return
        except:
            position = 0
            activeGame = False
            closed_poll = False
            activeTime = False
            auxVar2 = 0
            return

    def timer(self, timer):
        global next_poll
        global data_for_trivia
        global number_of_questions
        global position
        global activeGame
        global closed_poll
        global activeTime
        global player_score
        global auxVar2

        for i in range(timer):
            sleep(1)
        number_of_questions -= 1
        position += 1
        if (number_of_questions > 0):
            auxVar2 = 0
            self.trivia_time_handler2(data_for_trivia)
            Thread(target=self.timer(time)).start()
            return
        if (number_of_questions == 0):
                gchatid = poll_group_id
                winner_id = min(player_score, key=player_score.get)
                winner_user = retrieveUser(winner_id)
                winner_user.score += 1
                updateUser(chatID=winner_user.chatID, user=winner_user)
                data = ""
                ended_game = self.prepare_data_for_text(
                    data, '/code:', 'Juego terminado!, el ganador del juego fue {} con un puntaje de {}'.format(winner_user.nickname, player_score[winner_user.chatID]), "", gchatid)
                self.send_message(ended_game)
                position = 0
                activeGame = False
                closed_poll = False
                activeTime = False
                auxVar2 = 0
from difflib import SequenceMatcher
from firebase_admin import db
from firebase_admin import credentials
from itsObjects import *
import firebase_admin

from itsObjects.tutorialData import *

DEBUGFN = "[firebaseManagement]"


def startFirebase(firebase_url, certificate_file):
    """
    starts the firebase app

    Parameters
    ----------
        firebase_url : `str`
                firebase url from the db.
        certificate_file : `str`
                firebase certificate data.
    """
    DEBUGMN = "[startFirebase]"
    # load globals from the .env file
    # get firebase credentials
    firebase_sdk = credentials.Certificate(certificate_file)
    # start firebase app
    try:
        firebase_admin.initialize_app(
            firebase_sdk, {'databaseURL': firebase_url})
        prGreen(DEBUGFN+DEBUGMN+" firebase app started...")
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" error when trying to start the firebase app: {err}")


def detectNewUser(chatID, nickname):
    """
    detects a new user and adds it to the database.

    Parameters
    ----------
        chatID : `str`
                chat id of the new user.
        nickname : `str`
                new users firstname given by the Telegram API.

    Returns
    -------
        `bool`
            `True` if the user was saved correctly, `False` otherwise.
    """
    DEBUGMN = "[detectNewUser]"
    #startersubm = tutorial[0].submodules[0]
    usersDatabase = db.reference('/ID')
    prCyan(usersDatabase)
    snapshot = usersDatabase.order_by_key().get()
    if chatID not in snapshot:
        #new_user = User(chatID=chatID, score=0,
                        #hints=0, nickname=nickname)
        new_user = User(chatID=chatID, score=0,
                        nickname=nickname, attempts=0)
        try:
            #new_user.currentSubModule = startersubm
            usersDatabase.child(chatID).set(new_user.toJson())
            prGreen(DEBUGFN+DEBUGMN+f" User saved to the db.")
            return True
        except Exception as err:
            prRed(DEBUGFN+DEBUGMN +
                  f" Error when trying to save the user: {err}")
            return False
    prRed(DEBUGFN+DEBUGMN +
          f" User already in db")
    return False


def updateUser(chatID, user):
    """
    Takes the object user with the new data and replaces the old one with this data in firebase

    Parameters
    ---------
    chatID : `str`
    user : `User`

    Returns
    -------
    `bool`
        `True` if  successfull, `False` otherwisw
    """
    DEBUGMN = "[updateUser]"
    usersDatabase = db.reference(f'/ID/{chatID}')
    try:
        prCyan(DEBUGFN+DEBUGMN+f" {user.toJson()}")
        usersDatabase.set(user.toJson())
        prGreen(DEBUGFN+DEBUGMN+f" User data updated succesfully")
        return True
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" Error when updating the users data: {err}")
        return False


def pushModule(module, moduleNumber, submodules=[]):
    """
    adds a module to the database.

    Parameters
    ----------
        module : `Module`
                module to be added.
        moduleNumber : `Int`
                number of the module to be added.
        submodules`[Optional]` : `list of [SubModule]`
                list of the submodules of this module
    Returns
    -------
        `bool`
            `True` if the module was saved correctly, `False` otherwise.
    """
    DEBUGMN = "[pushModule]"
    modulesDatabase = db.reference('/Modules')
    if (len(submodules) != 0):
        module.submodules = submodules
    try:
        modulesDatabase.child(str(moduleNumber)).set(moduleToJson(module))
        prGreen(DEBUGFN+DEBUGMN +
                f" module name: {moduleToJson(module)['name']}, umbral: {moduleToJson(module)['umbral']}")
        prGreen(DEBUGFN+DEBUGMN+" module saved successfully")
        return True
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" error when adding the module: {err}")
        return False


def pushSubModule(submodule, moduleNumber, subModuleNumber):
    """
    adds a submodule to the modules table.

    Parameters
    ----------
        submodule : `SubModule`
                submodule to be added.
        moduleNumber : `Int`
                number of the module to be where this submodule belongs.
        subModuleNumber : `Int`
                number of the submodule to be added.
    Returns
    -------
        `bool`
            `True` if the submodule was saved correctly, `False` otherwise.
    """
    DEBUGMN = "[pushSubModule]"
    modulesDatabase = db.reference(f'/Modules/{moduleNumber}/submodules')
    try:
        modulesDatabase.child(str(subModuleNumber)).set(
            submoduleToJson(submodule))
        prGreen(DEBUGFN+DEBUGMN+f" submodule saved successfully")
        return True
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" error when adding the submodule: {err}")
        return False


def pushQuestion(question, moduleNumber, submoduleNumber):
    """
    adds a submodule to the modules table.

    Parameters
    ----------
        question : `Question`
                question to be added.
        moduleNumber : `Int`
                number of the module.
        submoduleNumber : `Str`
                number of the submodule where this question belongs.
    Returns
    -------
        `bool`
            `True` if the question was saved correctly, `False` otherwise.
    """
    DEBUGMN = "[pushQuestion]"
    modulesDatabase = db.reference(
        f'/Modules/{moduleNumber}/submodules/{submoduleNumber}')
    if question.q_type == 1:
        listToAddTo = 'alt_questions'
    else:
        listToAddTo = 'code_questions'
    try:
        modulesDatabase.child(listToAddTo).push(question.toJson())
        prGreen(DEBUGFN+DEBUGMN+f" question saved successfully")
        return True
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" error when adding the question: {err}")
        return False


def searchSender(pollID, questionAsked, questionType):
    """
    search the user who launched the pool from which the answer belongs to and returns it a given user

    Parameters
    ----------
        pollID : `Int`
                number of the chat id of the user to be retrieved.
        questionAsked : `Str`
                Question answered.
        questionType : `Int`
                Question type `[1 = Alternative|2 = Code]`
    Returns
    -------
        `User|None, Question|None`
            The retrieved user and question or `None` in case of error.
    """
    DEBUGMN = "[searchSender]"
    usersDatabase = db.reference('/ID')
    snapshot = usersDatabase.order_by_key().get()
    for us in snapshot:
        uspollId = usersDatabase.child(us).child('lastQuestionData').get()
        prCyan(f"uspollid:{uspollId}")
        if uspollId == None:
            continue
        if pollID == uspollId[0]:
            try:
                userfound = retrieveUser(us)
                prGreen(DEBUGFN+DEBUGMN+" User found!")
                if questionType == 1:
                    prGreen(DEBUGFN+DEBUGMN+" Alternative question")
                    prGreen(DEBUGFN+DEBUGMN+" questions:{}")
                    for altq in userfound.currentSubModule.alt_questions:
                        prCyan(DEBUGFN+DEBUGMN +
                               F"Searching question : {questionAsked}")
                        prCyan(DEBUGFN+DEBUGMN +
                               F"Question found in db : {altq.question}")
                        prCyan(DEBUGFN+DEBUGMN +
                               F"similarity ratio = {SequenceMatcher(None,altq.question,questionAsked).ratio()}")
                        if SequenceMatcher(None, altq.question, questionAsked).ratio() >= 0.8:
                            prGreen(DEBUGFN+DEBUGMN +
                                    f" question found!: {questionAsked}")
                            return userfound, altq
                for codeq in userfound.currentSubModule.code_questions:
                    if codeq.question == questionAsked:
                        prGreen(DEBUGFN+DEBUGMN +
                                f" question found!: {questionAsked}")
                        return userfound, codeq
                prRed(DEBUGFN+DEBUGMN+" No question was found")
                return None
            except Exception as err:
                prRed(DEBUGFN+DEBUGMN +
                      f" Error when trying to find user and/or question: {err}")
                return None
    prRed(DEBUGFN+DEBUGMN+" No User was found!!")
    return None


def retrieveModule(moduleNumber):
    """
    retrieves a given module

    Parameters
    ----------
        moduleNumber: `Int`
                number of the module to be retrieved.
    Returns
    -------
        `Tuple | None`
            the retrieved module or `None` in case of error.
    """
    DEBUGMN = "[retrieveModule]"
    modulesDatabase = db.reference('/Modules')
    try:
        moduleData = modulesDatabase.child(str(moduleNumber)).get()
        prGreen(DEBUGFN+DEBUGMN +
                f" Module {moduleData['name']} retrieved successfully")
        return jsonToModule(moduleData)
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" Error when trying to retrieve the module: {err}")
        return None


def retrieveUser(chatid):
    """
    retrieves a given user

    Parameters
    ----------
        chatid: `Int`
                number of the chat id of the user to be retrieved.

    Returns
    -------
        `User | None`
            The retrieved user or `None` in case of error.
    """
    DEBUGMN = "[retrieveUser]"
    usersDatabase = db.reference('/ID')
    try:
        userData = usersDatabase.child(str(chatid)).get()
        prCyan(userData)
        wantedUser = jsonToUser(userData)
        prCyan(DEBUGFN+DEBUGMN + f"user data: {userData}")
        if 'uq_history' in userData:
            wantedUser.uq_history = [jsonToQuestion(
                x) for x in wantedUser.uq_history]
        prGreen(DEBUGFN+DEBUGMN +
                f" User {userData['nickname']} retrieved successfully")
        return wantedUser
    except Exception as err:
        prRed(DEBUGFN+DEBUGMN +
              f" Error when trying to retrieve the user: {err}")
        return None

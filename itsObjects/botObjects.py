class User:
    """
    User that's currently using the bot to learn.

    Attributes
    ----------
        chatID : `str`
                Users telegram chat id return by the Telegram API whenever the user sends a message(doesn't includes Poll answers).
        score : `int`
                Users score on the current submodule.
        hints : `int`
                Number of hints taken by the user on the current submodule.
        qhint : `int [0=False|1=True]`
                whether the hint for this question has used already or not.
        nickname : `str`
                Users nickname given by the Telgram API.
        streak : `int`
                Users correct answers streak on the current submodule.
        qac : `int`
                Number of questions answered corretly by the user.
        qai : `int`
                Number of questions answered incorrectly by the user.
        qatsm : `int`
                Number of questions answered this submodule.
        cmodule : `int`
                Users current module index.
        csmodule : `int`
                Users current submodule index.
        uq_history : `list of [Question]`
                User answered questions list.
        us_history : `Dict`
                Users passed modules/submodules scores.
        lastQuestionId : 'Str'
                Users question answered ID.
        currentSubModule : 'SubModule'
                current SubModule that the user is answering.
        toJson : `dict`
                data parsed to Json format.
    """

    def __init__(self, chatID, score, nickname):
        self.chatID = chatID
        self.score = score
        #self.hints = hints
        #self.qhint = 0
        self.nickname = nickname
        self.streak = 0
        #self.qac = 0
        #self.qai = 0
        #self.qatsm = 0
        #self.cmodule = 1
        #self.csmodule = 1
        #self.uq_history = []
        #self.us_history = dict()
        #self.lastQuestionData = []
        #self.currentSubModule = ""

    def toJson(self):
        return {'chatID': self.chatID,
                'score': self.score,
                #'hints': self.hints,
                #'qhint': self.qhint,
                'nickname': self.nickname,
                'streak': self.streak,
                #'qac': self.qac,
                #'qai': self.qai,
                #'qatsm': self.qatsm,
                #'cmodule': self.cmodule,
                #'csmodule': self.csmodule,
                #'uq_history': [x.toJson() for x in self.uq_history],
                #'us_history': self.us_history,
                #'lastQuestionData': self.lastQuestionData,
                #'currentSubModule': submoduleToJson(self.currentSubModule)
                }


class Module:
    """
    Current module that the user is going through.

    Attributes
    ----------
        name : `str`
        umbral : `int`
                Minimum points needed to advance to the next module.
        submodules : `List of [Submodule]`
                This module submodules.
        toJson : `dict`
                data parsed to Json format.
    """

    def __init__(self, name, umbral):
        self.name = name
        self.umbral = umbral
        self.submodules = []

    def toJson(self):
        return {'name': self.name, 'umbral': self.umbral,
                'submodules': self.submodules}


class SubModule:
    """
    Current submodule that the user is going through.

    Attributes
    ----------
        name : `str`
        alt_questions : `List of [Question]`
                This submodule alternatives questions.
        toJson : `dict`
                data parsed to Json format.
    """

    def __init__(self, name, alt_questions):
        self.name = name
        self.alt_questions = alt_questions

    def toJson(self):
        return{'name': self.name, 'alt_questions': self.alt_questions}


class Question:
    """
    Question to be answered.

    Attributes
    ----------
        question : `str`
        q_type : `int`
                Question type: `1 = Alternative | 2 = Code`.
        difficulty : `int`
                Questions difficulty going from 1 to 3.
        answer : `int`
                If the question is of the type alterntives then is the index of the answer, else is "".
        hint : `int`
        alternatives`[Optional]` : `list of [Question]`
                Possible alternatives por this question.
        toJson : `dict`
                data parsed to Json format.
    """

    def __init__(self, question, answer, alternatives=[]):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives

    def toJson(self):
        return {'question': self.question,
                'q_type': self.q_type,
                'difficulty': self.difficulty,
                'answer': self.answer,
                'hint': self.hint,
                'alternatives': self.alternatives}


def submoduleToJson(submodule):
    """
    returns the submodule in Json format with its questions included

    Parameters
    ----------
    submodules : `SubModule`
                submodule tu be parsed

    Returns
    -------
    `Dict`
                the submodule in Json format
    """
    submJson = submodule.toJson()
    if len(submodule.alt_questions) != 0:
        altqJson = []
        for alt in submodule.alt_questions:
            altqJson.append(alt.toJson())
        submJson['alt_questions'] = altqJson

    if len(submodule.code_questions) != 0:
        codeqJson = []
        for code in submodule.code_questions:
            codeqJson.append(code.toJson())
        submJson['code_questions'] = codeqJson
    return submJson


def moduleToJson(module):
    """
    returns the module in Json format with its modules and submodules included

    Parameters
    ----------
    submodules : `Module`
                Module to be parsed.

    Returns
    -------
    `Dict`
                The module in Json format.
    """
    modJson = module.toJson()
    submJsonL = []
    for subm in module.submodules:
        submJsonL.append(submoduleToJson(subm))
    modJson['submodules'] = submJsonL
    return modJson


def jsonToQuestion(question):
    """
    parses the given `JSON` to a `Question`.

    Parameters
    ----------
        question: `Dict`
                Json with the question data.

    Returns
    -------
        `Question`
    """
    newQuestion = Question(question=question['question'], q_type=question['q_type'], difficulty=question['difficulty'],
                           answer=question['answer'], hint=question['hint'])

    if 'alternatives' in question:
        newQuestion.alternatives = question['alternatives']
    return newQuestion


def jsonToSubModule(submodule):
    """
    parses the given `JSON` to a `SubModule` including its `Questions`.

    Parameters
    ----------
        submodule: `Dict`
                Json with the submodule data.

    Returns
    -------
        `SubModule`
    """
    newSubModule = SubModule(submodule['name'], [], [], submodule['umbral'])
    if 'code_questions' in submodule:
        cquestions = []
        for codeq in submodule['code_questions']:
            cquestions.append(jsonToQuestion(codeq))
        newSubModule.code_questions = cquestions
    if 'alt_questions' in submodule:
        altquestions = []
        for altq in submodule['alt_questions']:
            altquestions.append(jsonToQuestion(altq))
        newSubModule.alt_questions = altquestions
    return newSubModule


def jsonToModule(module):
    """
    parses the given `JSON` to a `Module` including its `Submodules` and `Questions`.

    Parameters
    ----------
        module: `Dict`
                Json with the module data.

    Returns
    -------
        `Module`
    """
    newModule = Module(module['name'], module['umbral'])
    newModuleSubmL = []
    for subm in module['submodules']:
        newModuleSubmL.append(jsonToSubModule(subm))
    newModule.submodules = newModuleSubmL
    return newModule


def jsonToUser(user):
    """
    parses the given `JSON` to a `User` including its `SubModules`.

    Parameters
    ----------
        user: `Dict`
                Json with the user data.

    Returns
    -------
        `User`
    """
    #newUser = User(chatID=user['chatID'], score=user['score'],
    #               hints=user['hints'], nickname=user['nickname'])
    newUser = User(chatID=user['chatID'], score=user['score'],
                   nickname=user['nickname'])
    """
    newUser.qhint = user['qhint']
    newUser.streak = user['score']
    newUser.streak = user['streak']
    newUser.qac = user['qac']
    newUser.qai = user['qai']
    newUser.qatsm = user['qatsm']
    newUser.cmodule = user['cmodule']
    newUser.csmodule = user['csmodule']
    newUser.currentSubModule = jsonToSubModule(user['currentSubModule'])
    if 'lastQuestionData' in user:
        newUser.lastQuestionData = user['lastQuestionData']
    if 'uq_history' in user:
        newUser.uq_history = user['uq_history']
    if 'us_history' in user:
        newUser.us_history = user['us_history']
    """
    return newUser

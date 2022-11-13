from .botObjects import Module, SubModule, Question
DEBUGFN = "[tutorialData]"
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


# * <------------------------------- Trivia first mode	 ------------------------------->
m1 = Module(name="Trivia", umbral=13)
# * <----------------------- Submodule Variables ----------------------->
m2 = SubModule(name="Trivia", alt_questions=[])
# ? <-------------------- Questions -------------------->
qalternatives = ["Oliver Stone","Francis Ford Coppola","Stanley Kubrick","Michael Cimino"]
m2.alt_questions.append(Question(question="Who wrote and directed the 1986 film Platoon?",
                                      answer=0,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Homo Sapiens","Homo Ergaster","Homo Erectus","Homo Neanderthalensis"]
m2.alt_questions.append(Question(question="What is the scientific name for modern day humans?",
                                               answer=0,
                                               alternatives=qalternatives))

trivia = [m2]

def retrieveQuestions():
    """
    Retrieves a set of questions based on their type `[Alternative|Code]` and difficulty
    the last is considered only when `questionDifficulty` is given.
    Parameters
    ----------
    module : `int`
            module index from the 'tutorial' list that contains all the data.
    subModule : `int`
            subumodule index from the submodules list of the given module.
    Returns
    -------
    `Bool,List`
            `True,Question` if successfull, `False,None` otherwise.
    """
    DEBUGMN = "[retrieveQuestions]"
    module = 0
    subModule = 0
    prCyan(DEBUGFN+DEBUGMN +
               F" looking in module:{module} in submodule:{subModule} for an alternative question")
    wantedQuestions = trivia[module].alt_questions
    if len(wantedQuestions) == 0:
        prRed(DEBUGFN+DEBUGMN + " No questions found...")
        return False, None
    else:
        prGreen(DEBUGFN+DEBUGMN + " Success questions found " + str(wantedQuestions[0].question))
    return True, wantedQuestions
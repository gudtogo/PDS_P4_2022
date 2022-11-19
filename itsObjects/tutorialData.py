from .botObjects import Module, SubModule, Question
import random
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

qalternatives = ["Castor","Daedalus","Jason","Odysseus"]
m2.alt_questions.append(Question(question="Who in Greek mythology, who led the Argonauts in search of the Golden Fleece?",
                                      answer=2,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Wangan Midnight","Kino no Tabi","Cowboy Bebop", "Initial D"]
m2.alt_questions.append(Question(question="Which anime heavily features music from the genre 'Eurobeat'?",
                                               answer=3,
                                               alternatives=qalternatives))

qalternatives = ["Wheat","Bread","Milk","Egg"]
m2.alt_questions.append(Question(question="What ingredient is NOT used to craft a cake in Minecraft?",
                                      answer=1,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Activision","Konami","Electronic Arts","Harmonix"]
m2.alt_questions.append(Question(question="What company develops the Rock Band series of rhythm games?",
                                               answer=3,
                                               alternatives=qalternatives))

qalternatives = ["Tardar Sauce","Sauce","Minnie","Broccoli"]
m2.alt_questions.append(Question(question="What is Grumpy Cat's real name?",
                                      answer=0,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Gabriel Garcia Marquez","Jesus Quintero","Juan Joya Borga","Ernesto Guevara"]
m2.alt_questions.append(Question(question="What is the real name of the famous spanish humorist, El Risitas?",
                                               answer=2,
                                               alternatives=qalternatives))

qalternatives = ["Black","Brown","White","Yellow"]
m2.alt_questions.append(Question(question="What colour is the female blackbird?",
                                      answer=1,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Region","River","Country","City"]
m2.alt_questions.append(Question(question="What is Laos?",
                                               answer=2,
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
        
    random.shuffle(wantedQuestions)
    return True, wantedQuestions
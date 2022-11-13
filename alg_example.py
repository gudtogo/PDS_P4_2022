import random
from algorithmManage import *
from itsObjects import *


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


# test-user
user = User(0, 0, 0, 0, "tester")
# List with 6 pseudo-questions(3alternative/3code) for each sub_module. (24 questions)
questions = [Question("La libreria random", 1, 1, "answer1",
                      "hint1", ["alt11", "alt12", "alt13"]),
             Question("La libreria random2", 1, 2, "answer2",
                      "hint2", ["alt21", "alt22", "alt23"]),
             Question("La libreria random3", 1, 3, "answer3",
                      "hint3", ["alt31", "alt32", "alt33"]),
             Question("La libreria random_code", 2, 1, "answer1",
                      "hint1"),
             Question("La libreria random_code2", 2, 2, "answer2",
                      "hint2"),
             Question("La libreria random_code3", 2, 3, "answer3",
                      "hint3"),
             Question("Generar numeros enteros", 1, 1, "answer1",
                      "hint1", ["alt11", "alt12", "alt13"]),
             Question("Generar numeros enteros2", 1, 2, "answer2",
                      "hint2", ["alt21", "alt22", "alt23"]),
             Question("Generar numeros enteros3", 1, 3, "answer3",
                      "hint3", ["alt31", "alt32", "alt33"]),
             Question("Generar numeros enteros_code", 2, 1, "answer1",
                      "hint1"),
             Question("Generar numeros enteros_code2", 2, 2, "answer2",
                      "hint2"),
             Question("Generar numeros enteros_code3", 2, 3, "answer3",
                      "hint3"),
             Question("Generar numeros decimales", 1, 1, "answer1",
                      "hint1", ["alt11", "alt12", "alt13"]),
             Question("Generar numeros decimales2", 1, 2, "answer2",
                      "hint2", ["alt21", "alt22", "alt23"]),
             Question("Generar numeros decimales3", 1, 3, "answer3",
                      "hint3", ["alt31", "alt32", "alt33"]),
             Question("Generar numeros decimales_code", 2, 1, "answer1",
                      "hint1"),
             Question("Generar numeros decimales_code2", 2, 2, "answer2",
                      "hint2"),
             Question("Generar numeros decimales_code3", 2, 3, "answer3",
                      "hint3"),
             Question("Calcular eventos con probabilidad distinta", 1, 1, "answer1",
                      "hint1", ["alt11", "alt12", "alt13"]),
             Question("Calcular eventos con probabilidad distinta2", 1, 2, "answer2",
                      "hint2", ["alt21", "alt22", "alt23"]),
             Question("Calcular eventos con probabilidad distinta3", 1, 3, "answer3",
                      "hint3", ["alt31", "alt32", "alt33"]),
             Question("Calcular eventos con probabilidad distinta_code", 2, 1, "answer1",
                      "hint1"),
             Question("Calcular eventos con probabilidad distinta_code2", 2, 2, "answer2",
                      "hint2"),
             Question("Calcular eventos con probabilidad distinta_code3", 2, 3, "answer3",
                      "hint3")]
# List with the submodules
submodules = [SubModule(name="La libreria random", alt_questions=questions[0:3], code_questions=questions[3:6], umbral=2),
              SubModule(name="Generar números enteros",
                        alt_questions=questions[6:9], code_questions=questions[9:12], umbral=2),
              SubModule(name="Generar números decimales",
                        alt_questions=questions[12:15], code_questions=questions[15:18], umbral=2),
              SubModule(name="Calcular eventos con probabilidad distinta", alt_questions=questions[18:21], code_questions=questions[21:23], umbral=4)]
# Module
llr_module = Module("Generación de números aleatorios", 5)
# pass the submodules to the module
llr_module.submodules = submodules

for submodule in llr_module.submodules:
    finish = False
    cquestion_difficulty = -1  # -1 for the first question case
    while (not finish):
        if cquestion_difficulty == -1:  # first question
            cquestion_difficulty = questionDifficultyManagement(
                -1)
        else:
            cquestion_difficulty = questionDifficultyManagement(
                cquestion_difficulty)
        cquestion = questionTypeManagement(
            user.uq_history, submodule.alt_questions, submodule.code_questions, cquestion_difficulty)
        prCyan(
            f"Question: {cquestion.question} ; answer: {cquestion.answer} ; difficulty: {cquestion.difficulty}")
        your_answer = input("Your answer:")
        if(your_answer == "hint"):
            prGreen(f"Hint: {cquestion.hint}")
            user.score -= cquestion.difficulty*0.2
            your_answer = input("Your answer:")
        finish = questionPointsManagement(
            cquestion, your_answer, user, llr_module, submodule)[1]
    prCyan("<---------- Next Module ---------->")

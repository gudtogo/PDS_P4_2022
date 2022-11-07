import os
import dotenv
from itsObjects import *
from firebaseManage import startFirebase, pushModule, pushSubModule


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv()
FIREBASE_URL = os.getenv("FIREBASE_URL")
CERTIFICATE_FILE = os.getenv("CERTIFICATE_FILE")
startFirebase(FIREBASE_URL, CERTIFICATE_FILE)
# ! push Module para guardar modules , y pushSubModule para guardar submodulos
# ! si guardan los modulos , luego sus submodulos y luego sus preguntas en el archivo tutorialData,
# ! basta conque pusheen el module a la bdd y se guardara con sus submodulos y sus preguntas
# ! eso es lo recomendable,
# ! las funciones estan documentadas por si tienen dudas.
# TODO Run only if for whatever reason the questions need to be reuploaded to the fb.
pushModule(m1, 1, m1.submodules)
pushModule(m2, 2, m2.submodules)
pushModule(m3, 3, m3.submodules)
pushModule(m4, 4, m4.submodules)
pushModule(m5, 5, m5.submodules)
pushModule(m6, 6, m6.submodules)
pushModule(m7, 7, m7.submodules)
pushModule(m8, 8, m8.submodules)

from naoqi import ALProxy
from enum import Enum
import copy
# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
# pip install enum34

# Fin de partie égale

class Case(Enum):
	VIDE = 0
	PION_BLANC = 1
	PION_NOIR = 2
	DAME_BLANCHE = 3
	DAME_NOIRE = 4
	
class Etat(Enum):
	AUCUN = 0
	GAGNE = 1
	PERDU = 2
	EGALITE = 3
	
class Plateau:
	coups = 0
	etat = Etat.AUCUN
	
	obj = [[0 for x in range(10)] for y in range(10)] 
	
	def __init__(self):
		
	# Évalution du score du point de vue de l'IA
	def evaluation(self):
		return 0
	
	def listerLesCoupsPossibles(self):
		
	
	
class Coup:
	



tts = ALProxy("ALTextToSpeech", "127.0.0.1", 50766)
tts.say("Hello, world!")

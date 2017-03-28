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
	
# L'IA est toujours les blancs
class Tour(Enum):
	BLANC = 0
	NOIR = 1
	AUCUN = 2

class Action(Enum):
	AUCUN = 0
	MANGER = 1
	BOUGER = 2
	
def owner(case):
	if Case.PION_BLANC == case or Case.DAME_BLANCHE == case:
		return Tour.BLANC
	elif Case.PION_NOIR == case or Case.DAME_NOIRE == case:
		return Tour.NOIR
	else
		return Tour.AUCUN
		
def notOwner(case, pdv):
	tmp = owner(case)
	if(tmp != pdv and tmp != Tour.AUCUN):
		return true
	else
		return false
		
class Coup:
	coup_suivant = None
	pdv = Tour.AUCUN
	action = 
	
class Plateau:
	coups = 0
	etat = Etat.AUCUN
	tour = Tour.BLANC # Les blancs commencent
	nbr_pions_blancs = 20
	nbr_pions_noirs = 20
	
	obj = [[0 for x in range(10)] for y in range(10)] # 0,0 <=> en bas à gauche
	
	def __init__(self):
		
	# Évalution du score du point de vue de l'IA
	def evaluation(self):
		score = 0
		
		if(self.etat == Etat.GAGNE):
			score += 1000 + (self.coups * 10) # Il faut gagner le plus rapidement possible
		elif(self.etat == Etat.PERDU):
			score -= 1000 - (self.coups * 10) # Si la défaite est inévitable, il faut perdre le plus lentement
		else:
			score -= self.coups * 10
	
	
		return score
	
	def listerLesCoupsPossibles(self, pdv):
		coups = []
		for i in range(0, 10):
			for j in range(0, 10):
				if(owner(self.obj[i][j]) == pdv):
					coups += makeMoves(i, j, pdv)
		return coups
		
	# Un pion ne peut faire qu'avancer s'il ne manger pas
	def validerBouger(y, pdv):
		if((pdv == Tour.BLANC and y == 1) or (pdv == Tour.NOIR and y == -1)):
			return true
		else
			return false
	
	def canEatOrMove(self, i, j, x, y, pdv):
		if(0 <= i + x <= 10 and 0 <= j + y <= 10):
			if(notOwner(self.obj[i + x][j + y]) and 0 <= i + 2 * x < 10 and 0 <= j + 2 * y <= 10):
				if(owner(self.obj[i + 2 * x][j + 2 * y]) == Tour.AUCUN):
					return Action.MANGER
			elif(validerBouger(y, pdv) and owner(self.obj[i + x][j + y]) == Tour.AUCUN):
				return Action.BOUGER
		return Action.AUCUN
	
	def makeMoves(self, i, j, pdv):
		liste = []
		if(canEat(i, j, -1, -1, pdv)):
			liste += new Coup()....
		
		return liste


tts = ALProxy("ALTextToSpeech", "127.0.0.1", 50766)
tts.say("Hello, world!")

from naoqi import ALProxy
# from enum import Enum

# class Case(Enum):
	# VIDE = 0
	# PION_BLANC = 1
	# PION_NOIR = 2
	# DAME_BLANCHE = 3
	# DAME_NOIRE = 4
	
# Plateau = [[0 for x in range(10)] for y in range(10)] 

tts = ALProxy("ALTextToSpeech", "127.0.0.1", 50766)
tts.say("Hello, world!")

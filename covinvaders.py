import pygame
import time
import Virus
import Boss
import Player
import random
import os
import pygame, random, sys
from pygame.locals import *



# POUR CHAQUE NIVEAU/BOSS, ON FAIT UNE CLASSE ABSTRAITE NOMMEE GAMESCREEN, ET 2 SOUS CLASSES BOSS_SCREEN ET VIRUS_SCREEN
# POUR MODELISER CHAQUE ECRAN DE JEU SANS REPETER LES DIMENSIONS ET SANS REPETER DU CODE PR RIEN, ET AUSSI
# ON AURAIT JUSTE A CHANGER LA PHOTO DE FOND, LE TYPE DENNEMI, ET LIMAGE DU BOSS, ET UNE CLASSE PR LES ECRANS AVEC TEXT
# PAS OUBLIER DY METTRE LES BONUS ET LES BPNUS SPECIFIQUES AUX ECRANS VIRUS ET CEUX SPECIFIQUES AU NIVEAUX BOSS

#Taille fenetre
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

#Taille Virus
RED_VIRUS_SIZE = 20
GREEN_VIRUS_SIZE = 30
PURPLE_VIRUS_SIZE = 40
BLUE_VIRUS_SIZE = 50 #frozen


#Charge l'image des virus
redVirusImage = pygame.image.load('covinv_docs/red_virus.png') # ---------------> MODIF DE REMY : CHARGE CORONA IMAGE

#Rect(left, top, width, height) -> Rect
redVirRect = pygame.Rect(random.randint(0, WINDOW_WIDTH - RED_VIRUS_SIZE), 0 - RED_VIRUS_SIZE, RED_VIRUS_SIZE, RED_VIRUS_SIZE)

#CHAUVE SOURIS
BatBossImage = pygame.image.load('covinv_docs/pngegg.png')
BatBossRect = BatBossImage.get_rect()
BatBossRect.topleft = (WINDOW_WIDTH-500, WINDOW_HEIGHT-600)


# lance pygame, ouvre la fenetre de jeu et active le curseur de la souris
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False) #curseur souris visible, mais je sais pas si on en a besoin

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

import pygame
import time
import random
import os

#Taille fenetre
WINDOWHEIGHT = 600
WINDOWWIDTH = 600

#Charge l'image des virus
redVirusImage = pygame.image.load('docs/coronavirus.png') # ---------------> MODIF DE REMY : BADDIE = CORONA

#CHAUVE SOURIS
BatBossImage = pygame.image.load('docs/pngegg.png')
BatBossRect = BatBossImage.get_rect()
BatBossRect.topleft = (WINDOWWIDTH-500, WINDOWHEIGHT-600)

# lance pygame, ouvre la fenetre de jeu et active le curseur de la souris
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)
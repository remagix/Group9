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
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")

#Images
#Charge l'image des virus
redVirusImage = pygame.image.load('covinv_docs/red_virus.png')
greenVirusImage = pygame.image.load('covinv_docs/green_virus.png')
blueVirusImage = pygame.image.load('covinv_docs/blue_virus.png')
purpleVirusImage = pygame.image.load('covinv_docs/purple_virus.png')

#charge l'image du joueur
#PlayerImage = pygame.image,load()

#Charge L'image des boss
BatbossImage = pygame.image,load('covinv_docs/pngegg.png')
#TrumpbossImage = pygame.image,load()
#PangolinbossImage = pygame.image,load()

#Charge L'image des objets
#MaskImage = pygame.image,load()
#VaccineImage = pygame.image,load()
#AmmoImage = pygame.image,load()
#Trav_CertImage = pygame.image,load()

#Charge L'image des tirs
#PlayermissileImage = pygame.image,load()
#BatmissileImage = pygame.image,load()
#TrumpmissileImage = pygame.image,load()
#PangolinmissileImage = pygame.image,load()

#Charge L'image de l'arrière plan

#StartBGImage = pygame.image,load()
#MenuBGImage = pygame.image,load()
#PauseBGImage = pygame.image,load()
#EndBGImage = pygame.image,load()
#Wave_OneBGImage = pygame.image,load()
#Wave_TwoBGImage = pygame.image,load()
#Wave_ThreeBGImage = pygame.image,load()
#Boss_OneBGImage = pygame.image,load()
#Boss_TWOBGImage = pygame.image,load()
#Boss_ThreeBGImage = pygame.image,load()
#Story_OneBGImage = pygame.image,load()
#Story_TwoBGImage = pygame.image,load()
#Story_ThreeBGImage = pygame.image,load()
#Story_FourBGImage = pygame.image,load()
#Story_FiveBGImage = pygame.image,load()
#Story_SixBGImage = pygame.image,load()
#Story_SevenBGImage = pygame.image,load()

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        #WINDOW.blit(BG)

        pygame.display.update()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if event.key == K_ESCAPE:
                        run = False
main()



#Taille Virus
RED_VIRUS_SIZE = 20
GREEN_VIRUS_SIZE = 30
PURPLE_VIRUS_SIZE = 40
BLUE_VIRUS_SIZE = 50 #frozen




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

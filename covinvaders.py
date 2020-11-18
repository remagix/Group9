import pygame
import time
import Boss
import Player
import random
import os
import pygame, random, sys
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()


# POUR CHAQUE NIVEAU/BOSS, ON FAIT UNE CLASSE ABSTRAITE NOMMEE GAMESCREEN, ET 2 SOUS CLASSES BOSS_SCREEN ET VIRUS_SCREEN
# POUR MODELISER CHAQUE ECRAN DE JEU SANS REPETER LES DIMENSIONS ET SANS REPETER DU CODE PR RIEN, ET AUSSI
# ON AURAIT JUSTE A CHANGER LA PHOTO DE FOND, LE TYPE DENNEMI, ET LIMAGE DU BOSS, ET UNE CLASSE PR LES ECRANS AVEC TEXT
# PAS OUBLIER DY METTRE LES BONUS ET LES BPNUS SPECIFIQUES AUX ECRANS VIRUS ET CEUX SPECIFIQUES AU NIVEAUX BOSS

pygame.mixer.music.load('covinv_docs/Magic System- Premier Gaou.mp3.mid')

#Taille fenetre
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")

#Images
#Charge l'image des virus
redVirusImage = pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/red_virus.png')),(50,50))
greenVirusImage = pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/green_virus.png')),(50,50))
blueVirusImage = pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/blue_virus.png')),(50,50))
purpleVirusImage = pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/purple_virus.png')),(50,50))
#test
test = redVirusImage.get_rect()


#charge l'image du joueur

#PlayerImage = pygame.image,load()

#Charge L'image des boss
BatbossImage= pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#BatbossImage = pygame.image.load('covinv_docs/pngegg.png')
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

StartBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/phototest.jpg')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#MenuBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#PauseBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#EndBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Wave_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Wave_TwoBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Wave_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Boss_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Boss_TWOBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Boss_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_TwoBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_FourBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_FiveBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_SixBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
#Story_SevenBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))

class Virus:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.health = None
      self.virus_img = None
  def draw(self, window):
      WINDOW.blit(self.virus_img,(self.x, self.y))
  def update(self):
      pygame.event.pump()

class Character(Virus):
  def __init__(self,x ,y):
      super().__init__(x,y)
      self.virus_img = redVirusImage
      self.laser_img = None

class Colorvirus(Virus):
  Virus_MAP = {
              "red" : (redVirusImage),
              "green" : (greenVirusImage ),
              "blue" : (blueVirusImage ),
              "purple" : (purpleVirusImage)
              }

  def __init__(self,x ,y, color):
      super().__init__(x,y)
      self.virus_img = self.Virus_MAP[color]
  def move(self, vel):
      self.y += vel
def main():
  run = True
  FPS = 60
  level = 1
  lives = 10
  main_font = pygame.font.SysFont("timesnewroman", 20)
  lost_font = pygame.font.SysFont("timesnewroman", 30)
  enemies = []
  wave_length = 30
  virus_vel = 4

  character = Character(300, 500)

  clock = pygame.time.Clock()
  lost = False

  def redraw_window():
      WINDOW.blit(StartBGImage, (0,0))
      WINDOW.blit(BatbossImage, (150,0))
      pygame.draw.line(WINDOW,(255,0,0), (0,450),(600,450), 3)
      #draw text
      lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 255))
      level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))


      WINDOW.blit(lives_label, (10, 10))
      WINDOW.blit(level_label, (WINDOW_WIDTH - level_label.get_width() - 10, 10))

      for enemy in enemies:
          enemy.draw(WINDOW)

      character.draw(WINDOW)

      if lost == True:
          lost_label = lost_font.render("You have been infected", 1 ,(0,255,0))
          lost_label2 = lost_font.render("You lost", 1, (0, 255, 0))
          WINDOW.blit(lost_label, (WINDOW_WIDTH/2 - lost_label.get_width()/2, 300))
          WINDOW.blit(lost_label2, (WINDOW_WIDTH / 2 - lost_label.get_width() / 2, 340))

      pygame.display.update()
  pygame.mixer.music.play(-1, 0, 0)

  while run:
      clock.tick(FPS)
      if lives <= 0:
          lost = True
      if len(enemies) == 0:
          for i in range(wave_length):
              enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH-100), random.randrange(-1000,-100), random.choice(["red", "blue", "green", "purple"]))
              enemies.append(enemy)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
          if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  run = False



      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and character.x - 5 > 0:
          character.x -= 5
      if keys[pygame.K_RIGHT] and character.x + 5 + character.virus_img.get_width() < WINDOW_WIDTH:
          character.x += 5
      if keys[pygame.K_UP] and character.y - 5 > 0:
          character.y -= 5
      if keys[pygame.K_DOWN] and character.y + 5 + character.virus_img.get_height() < WINDOW_HEIGHT:
          character.y += 5

      for enemy in enemies[:]:
          enemy.move(virus_vel)
          if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
              lives -= 1
              enemies.remove(enemy)
      redraw_window()
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

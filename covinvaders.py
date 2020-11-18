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

pygame.mixer.music.load('covinv_docs/Magic System- Premier Gaou.mp3')

#Taille fenetre
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")

#Images
#Charge l'image des virus
redVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/red_virus.png'),(50,50))
greenVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/green_virus.png'),(50,50))
blueVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/blue_virus.png'),(50,50))
purpleVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/purple_virus.png'),(50,50))

#SANI-GUN
drop_img = pygame.transform.scale(pygame.image.load('covinv_docs/drop.png'), (20, 20))

#POINTS DE VIE DES DIFFERENTS VIRUS
HP_RED = 2
HP_GREEN = 3
HP_BLUE = 4
HP_PURPLE = 5


#charge l'image du joueur

#PlayerImage = pygame.image,load()

#Charge L'image des boss
BatbossImage= pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))


#Charge L'image des objets

#MaskImage = pygame.image,load()
#VaccineImage = pygame.image,load()
#AmmoImage = pygame.image,load()
travCertImage = pygame.transform.scale(pygame.image.load('cherry.png'), (50, 50))
freezingImage = pygame.transform.scale(pygame.image.load('covinv_docs/freezing.png'), (40, 40))

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


  def draw(self, window): #WINDOW ou window ?
      WINDOW.blit(self.virus_img,(self.x, self.y))

  def update(self):
      pygame.event.pump()

  #def collide(obj1, obj2):
   #   offset_x = obj2.x - obj1.x
    #  offset_y = obj2.y - obj1.y
     # return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

   # def collision(self, obj):
    #    return Virus.collide(self, obj)





class Character:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.health = None
      self.character_img = redVirusImage
      self.bullets = []
      self.shoot_img = drop_img


  def draw(self, window):
      WINDOW.blit(self.character_img,(self.x, self.y))
      for bullet in self.bullets:
          bullet.draw(window)

  def move_bullets(self, vel, obj):
      for bullet in self.bullets:
          bullet.move(vel)
          if bullet.off_screen(WINDOW_HEIGHT):
              self.bullets.remove(bullet)
          #elif bullet.collision(obj):
            #  obj.health -= 10
            #  self.bullets.remove(bullet)

  def update(self):
      pygame.event.pump()

  def shoot(self):
      standard_ammo = Bullet(self.x, self.y, self.shoot_img)
      self.bullets.append(standard_ammo)




class Colorvirus(Virus):
  Virus_MAP = {
              "red" : redVirusImage,
              "green" : greenVirusImage,
              "blue" : blueVirusImage,
              "purple" : purpleVirusImage
              }

  Health_Map = {
                "red" : HP_RED,
                "green" : HP_GREEN,
                "blue" : HP_BLUE,
                "purple" : HP_PURPLE
                }

  def __init__(self, x, y, color):
      super().__init__(x, y)
      self.virus_img = self.Virus_MAP[color]
      self.health = self.Health_Map[color]

  def move(self, vel):
      self.y += vel


class Items(Virus):
    Items_MAP = {
        "mask": redVirusImage,
        "vaccine": greenVirusImage,
        "ammo": blueVirusImage,
        "trav_cert": travCertImage,
        "freeze" : freezingImage
    }


def main():
  run = True
  FPS = 60
  level = 1
  lives = 50
  main_font = pygame.font.SysFont("timesnewroman", 20)
  lost_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
  enemies = []
  wave_length = 10
  wave = 0
  virus_vel = 4
  shoot_vel = 5

  character = Character(300, 500)

  clock = pygame.time.Clock()
  lost = False

  def stop():
      lost_label = lost_font.render("You have been infected", 1, (86, 189, 5))
      lost_label2 = lost_font.render("You lost", 1, (86, 189, 5))
      WINDOW.blit(lost_label, (WINDOW_WIDTH / 2 - lost_label.get_width() / 2, 260))
      WINDOW.blit(lost_label2, (WINDOW_WIDTH / 2 - lost_label2.get_width() / 2, 300))
      pygame.mixer.music.stop()
      pygame.mixer.music.load('covinv_docs/Despi.mid')
      pygame.mixer.music.play(-1, 0, 0)
      while lost:
          for event in pygame.event.get():

              if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()

          pygame.display.update()
          clock.tick(15)

  def redraw_window():
      WINDOW.blit(StartBGImage, (0,0))
      WINDOW.blit(BatbossImage, (150,0))
      pygame.draw.line(WINDOW,(255,0,0), (0,450),(600,450), 3)
      #draw text
      lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 255))
      level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
      wave_label = main_font.render(f"Wave: {wave}", 1, (255, 255, 255))

      WINDOW.blit(lives_label, (10, 10))
      WINDOW.blit(level_label, (WINDOW_WIDTH - level_label.get_width() - 10, 10))
      WINDOW.blit(wave_label, (WINDOW_WIDTH / 2 - wave_label.get_width() / 2, 10))

      for enemy in enemies:
          enemy.draw(WINDOW)

      character.draw(WINDOW)



      pygame.display.update()
  pygame.mixer.music.play(-1, 0, 0)

  i = 0
  while run:
      i+=1
      clock.tick(FPS)
      if lives <= 0:
          lost = True
          stop()
      if len(enemies) == 0:
          for i in range(wave_length):
              enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH-100), random.randrange(-1200, -300), random.choice(["red", "blue", "green", "purple"]))
              enemies.append(enemy)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
          if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  run = False
      if i%20 == 0:
          character.shoot()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and character.x - 5 > 0:
          character.x -= 5
      if keys[pygame.K_RIGHT] and character.x + 5 + character.character_img.get_width() < WINDOW_WIDTH:
          character.x += 5
      if keys[pygame.K_UP] and character.y - 5 > 0:
          character.y -= 5
      if keys[pygame.K_DOWN] and character.y + 5 + character.character_img.get_height() < WINDOW_HEIGHT:
          character.y += 5

      for enemy in enemies[:]:
          enemy.move(virus_vel)
          if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
              lives -= 1
              enemies.remove(enemy)
      character.move_bullets(-shoot_vel, enemies)
      redraw_window()
main()









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

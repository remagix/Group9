import pygame
import time
import random
import os
import pygame
import random
import sys
from pygame.locals import *

pygame.font.init()
pygame.mixer.init()

# POUR CHAQUE NIVEAU/BOSS, ON FAIT UNE CLASSE ABSTRAITE NOMMEE GAMESCREEN, ET 2 SOUS CLASSES BOSS_SCREEN ET VIRUS_SCREEN
# POUR MODELISER CHAQUE ECRAN DE JEU SANS REPETER LES DIMENSIONS ET SANS REPETER DU CODE PR RIEN, ET AUSSI
# ON AURAIT JUSTE A CHANGER LA PHOTO DE FOND, LE TYPE DENNEMI, ET LIMAGE DU BOSS, ET UNE CLASSE PR LES ECRANS AVEC TEXT
# PAS OUBLIER DY METTRE LES BONUS ET LES BPNUS SPECIFIQUES AUX ECRANS VIRUS ET CEUX SPECIFIQUES AU NIVEAUX BOSS

pygame.mixer.music.load('covinv_docs/Dior.mp3')

# Taille fenetre
FPS = 60
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")

# Images
# Charge l'image des virus
redVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/red_virus.png'), (50, 50))
greenVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/green_virus.png'), (50, 50))
blueVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/blue_virus.png'), (50, 50))
purpleVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/purple_virus.png'), (50, 50))

# SANI-GUN
drop_img = pygame.transform.scale(pygame.image.load('covinv_docs/drop.png'), (20, 20))

# POINTS DE VIE DES DIFFERENTS VIRUS
HP_RED = 2
HP_GREEN = 3
HP_BLUE = 4
HP_PURPLE = 5

# charge l'image du joueur

heroImage = pygame.transform.scale(pygame.image.load('covinv_docs/samus.png'), (70, 90))

# Charge L'image des boss
batBossImage = pygame.transform.scale(pygame.image.load('covinv_docs/bossUS.png'),
                                   (200, 200))
angryTrumpImage = pygame.transform.scale(pygame.image.load('covinv_docs/ANGRY BOSS US.png'),
                                   (200, 200))

# Charge L'image des objets

maskImage = pygame.transform.scale(pygame.image.load('covinv_docs/medical-mask.png'), (50, 50))
vaccineImage = pygame.transform.scale(pygame.image.load('covinv_docs/syringe.png'), (50, 50))
bonusAmmoImage = pygame.transform.scale(pygame.image.load('covinv_docs/ammo.png'), (50, 50))
travCertImage = pygame.transform.scale(pygame.image.load('covinv_docs/certification.png'), (50, 50))
freezingImage = pygame.transform.scale(pygame.image.load('covinv_docs/freezing.png'), (40, 40))

# Charge L'image des tirs

# BatmissileImage = pygame.image,load()
# TrumpmissileImage = pygame.image,load()
# PangolinmissileImage = pygame.image,load()

# Charge L'image de l'arrière plan

startBGImage = pygame.transform.scale(pygame.image.load('covinv_docs/phototest.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
jungle_BG = pygame.transform.scale(pygame.image.load('covinv_docs/test_BG.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))

# MenuBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# PauseBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# EndBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Wave_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Wave_TwoBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Wave_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Boss_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Boss_TWOBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Boss_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_OneBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_TwoBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_ThreeBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_FourBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_FiveBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_SixBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))
# Story_SevenBGImage =  pygame.transform.scale(pygame.image.load(os.path.join('covinv_docs/pngegg.png')),(WINDOW_WIDTH,WINDOW_HEIGHT))

class Falling:
 def __init__(self, x, y):
     self.x = x
     self.y = y
     self.falling_img = None

 def draw(self, window):
     window.blit(self.falling_img, (self.x, self.y))

 def update(self):
     pygame.event.pump()



class Virus(Falling):

 def __init__(self, x, y):
     super().__init__(x, y)
     self.health = None
     self.virus_img = None

 def draw(self, window):
     window.blit(self.virus_img, (self.x, self.y))

 def update(self):
     super().update()

 def move(self, vel):
     self.y += vel


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
     return not (height >= self.y >= 0)

 def collision(self, obj):
     return collide(self, obj)


class Character:

 def __init__(self, x, y):
     self.x = x
     self.y = y
     self.health = None
     self.character_img = None
     self.mask = None
     self.bullets = []
     self.bullet_img = None

 #def shoot
 #def move_bullets


 #def draw

 def update(self):
     pygame.event.pump()


class Boss(Character):

 def __init__(self, x, y):
     super(Boss, self).__init__(x, y)
     self.boss_img = batBossImage
     self.bullet_img = redVirusImage
     self.bullets = []
     self.health = 50
     self.mask = pygame.mask.from_surface(self.boss_img)
     self.hasard = random.choice([2,-2])

 def draw(self, window):
     window.blit(self.boss_img, (self.x, self.y))
     for bullet in self.bullets:
         bullet.draw(window)

 def move_bullets(self, vel, hero):
     for bullet in self.bullets:
         bullet.move(-vel)
         if bullet.off_screen(WINDOW_HEIGHT):
             self.bullets.remove(bullet)
         else:
             if bullet.collision(hero):
                 if hero.lives - 1 > 0:
                     hero.lives -= 1
                 if bullet in self.bullets:
                     self.bullets.remove(bullet)

 def update(self):
     super().update()

 def shoot(self):
     boss_ammo = Bullet(random.choice([self.x + 10, self.x + 190]), self.y + 100, self.bullet_img)
     self.bullets.append(boss_ammo)

 def move(self, vel):
     if self.x <= 0:
         self.x += vel
         self.hasard = vel
     elif self.x > 0 and self.x < 100:
         self.x += self.hasard
     elif self.x == 100:
         self.hasard = random.choice([vel, -vel])
         self.x += self.hasard
     elif self.x > 100 and self.x < 200:
         self.x += self.hasard
     elif self.x == 200:
         self.hasard = random.choice([vel, -vel])
         self.x += self.hasard
     elif self.x > 200 and self.x < 300:
         self.x += self.hasard
     elif self.x == 300:
         self.hasard = random.choice([vel, -vel])
         self.x += self.hasard
     elif self.x > 300 and self.x < WINDOW_WIDTH - batBossImage.get_width():
         self.x += self.hasard

     elif self.x >= WINDOW_WIDTH - batBossImage.get_width():
         self.x -= vel
         self.hasard = -vel





class Hero(Character):

 def __init__(self, x, y):
     super(Hero, self).__init__(x, y)
     self.hero_img = heroImage
     self.mask = pygame.mask.from_surface(self.hero_img)
     self.bullet_img = drop_img
     self.lives = 50

 def draw(self, window):
     window.blit(self.hero_img, (self.x, self.y))
     for bullet in self.bullets:
         bullet.draw(window)

 def move_bullets(self, vel, objs):
     for bullet in self.bullets:
         bullet.move(vel)
         if bullet.off_screen(WINDOW_HEIGHT):
             self.bullets.remove(bullet)
         else:
             for obj in objs:
                 if bullet.collision(obj):
                     if obj.health - 1 == 0:
                         objs.remove(obj)
                     else:
                         obj.health -= 1
                     if bullet in self.bullets:
                         self.bullets.remove(bullet)


 def move_bullets_vs_boss(self, vel, boss):
     for bullet in self.bullets:
         bullet.move(vel)
         if bullet.off_screen(WINDOW_HEIGHT):
             self.bullets.remove(bullet)
         else:
             if bullet.collision(boss):
                 if boss.health - 1 == 0:
                     main_start() #je sais pas quoi mettre ici pr passer a la suite
                 else:
                     boss.health -= 1
                 if bullet in self.bullets:
                     self.bullets.remove(bullet)

 def update(self):
     super().update()

 def shoot(self):
     standard_ammo = Bullet(self.x + 8, self.y - 20, self.bullet_img)
     self.bullets.append(standard_ammo)


class Colorvirus(Virus):

 def __init__(self, x, y, color, hp):
     super().__init__(x, y)
     self.virus_img = self.Virus_MAP[color]
     self.mask = pygame.mask.from_surface(self.virus_img)
     self.health = self.Health_Map[hp]

 Virus_MAP = {
     "red": redVirusImage,
     "green": greenVirusImage,
     "blue": blueVirusImage,
     "purple": purpleVirusImage
 }

 Health_Map = {
     "red": HP_RED,
     "green": HP_GREEN,
     "blue": HP_BLUE,
     "purple": HP_PURPLE
 }


class Items(Falling):

 Items_MAP = {
     "mask": maskImage,
     "vaccine": vaccineImage,
     "ammo": bonusAmmoImage,
     "trav_cert": travCertImage,
     "freeze": freezingImage
 }

 def __init__(self, x, y):
     super().__init__(x, y)
     self.bonus_img = None

 def draw(self, window):
     window.blit(self.bonus_img, (self.x, self.y))

 def update(self):
     super().update()


def collide(obj1, obj2):
 diff_x = obj2.x - obj1.x
 diff_y = obj2.y - obj1.y
 return obj1.mask.overlap(obj2.mask, (diff_x, diff_y)) is not None


def main():

 run = True
 level = 1
 main_font = pygame.font.SysFont("timesnewroman", 20)
 lost_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
 enemies = []
 wave_length = 10
 wave = 0
 virus_vel = 5
 bullet_vel = 5
 boss_vel = 2

 hero = Hero(300, 500)
 batBoss = Boss(200, 0)

 clock = pygame.time.Clock()
 lost = False

 def stop():
     lost_label = lost_font.render("You have been infected", 1, (86, 189, 5))
     lost_label2 = lost_font.render("You lost (press key)", 1, (86, 189, 5))

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
             if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                     pygame.quit()
                     quit()
                 else:
                     pygame.mixer.music.stop()
                     pygame.mixer.music.load('covinv_docs/Dior.mp3')
                     main_start()
                     break
         pygame.init()
         pygame.display.update()
         clock.tick(15)

 def redraw_window():
     WINDOW.blit(BG, (0, 0))
     pygame.draw.line(WINDOW, (255, 0, 0), (0, 450), (600, 450), 3)
     # draw text
     lives_label = main_font.render(f"Lives: {hero.lives}", 1, (255, 0, 255))
     level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
     wave_label = main_font.render(f"Wave: {wave}", 1, (255, 255, 255))

     WINDOW.blit(lives_label, (10, 10))
     WINDOW.blit(level_label, (WINDOW_WIDTH - level_label.get_width() - 10, 10))
     WINDOW.blit(wave_label, (WINDOW_WIDTH / 2 - wave_label.get_width() / 2, 10))

     for enemy in enemies:
         enemy.draw(WINDOW)

     hero.draw(WINDOW)
     if level == 2:
         batBoss.draw(WINDOW)
     pygame.display.update()

 hero_cooldown = 0
 boss_cooldown = 0
 while run:
     hero_cooldown += 1
     clock.tick(FPS)
     if hero.lives <= 0:
         lost = True
         stop()
     if level == 1:
         BG = startBGImage
         if len(enemies) == 0:
             wave += 1
             wave_length += 5
             if wave == 1:
                 for i in range(wave_length):
                     randVirus = random.choice(["red", "green"])
                     enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1200, -300), randVirus,
                                        randVirus)
                     enemies.append(enemy)
         for enemy in enemies[:]:
             enemy.move(virus_vel)
             if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
                 hero.lives -= 1
                 enemies.remove(enemy)
         if wave == 2:
             level = 2
     if level == 2:
         boss_cooldown += 1
         BG = jungle_BG
         if batBoss.health > 25:
             batBoss.move(boss_vel)
             if boss_cooldown % 100 == 0:
                 batBoss.shoot()
         else:
             batBoss.boss_img = angryTrumpImage
             batBoss.move(boss_vel*2)
             if boss_cooldown % 50 == 0:
                 batBoss.shoot()
         batBoss.move_bullets(-bullet_vel, hero)
         hero.move_bullets_vs_boss(-bullet_vel, batBoss)

     for event in pygame.event.get():
         if (event.type == pygame.QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
             run = False
             quit() # le quit ici fait que le jeu quitte, sans cela on retourne a l'ecran de depart pour recommencer

     if hero_cooldown % 20 == 0:
         hero.shoot()

     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and hero.x - 5 > 0:
         hero.x -= 5
     if keys[pygame.K_RIGHT] and hero.x + 5 + hero.hero_img.get_width() < WINDOW_WIDTH:
         hero.x += 5
     if keys[pygame.K_UP] and hero.y - 5 > 450:
         hero.y -= 5
     if keys[pygame.K_DOWN] and hero.y + 5 + hero.hero_img.get_height() < WINDOW_HEIGHT:
         hero.y += 5

     hero.move_bullets(-bullet_vel, enemies)

     redraw_window()


def main_start():
 pygame.init()
 run = True
 title_font = pygame.font.SysFont("comicsans", 30)
 pygame.mixer.music.play(-1, 0, 0)
 while run:
     WINDOW.blit(startBGImage, (0, 0))
     title_label = title_font.render("Press any key to go to war...", 1, (255, 255, 255))
     WINDOW.blit(title_label, (WINDOW_WIDTH/2 - title_label.get_width()/2, 350))
     pygame.display.update()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             run = False
         if event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 run = False
             else:
                 main()
 pygame.quit()



main_start()



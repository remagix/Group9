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




FPS = 60
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")


redVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/red_virus.png'), (50, 50))
greenVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/green_virus.png'), (50, 50))
blueVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/blue_virus.png'), (50, 50))
purpleVirusImage = pygame.transform.scale(pygame.image.load('covinv_docs/purple_virus.png'), (50, 50))


drop_img = pygame.transform.scale(pygame.image.load('covinv_docs/drop.png'), (20, 20))
pangbat_img = pygame.transform.scale(pygame.image.load('covinv_docs/missilelittlebat.png'), (80, 80))
batgrnfire_img = pygame.transform.scale(pygame.image.load('covinv_docs/grnfire.png'), (80, 80))
batredfire_img = pygame.transform.scale(pygame.image.load('covinv_docs/redfire.png'), (80, 80))
dynamiteUS_img = pygame.transform.scale(pygame.image.load('covinv_docs/dynamite.png'), (70, 70))
nukeUS_img = pygame.transform.scale(pygame.image.load('covinv_docs/nukeUS.png'), (80, 80))
minibat_img = pygame.transform.scale(pygame.image.load('covinv_docs/pngegg.png'), (80, 56))

HP_RED = 1
HP_GREEN = 2
HP_BLUE = 3
HP_PURPLE = 4


heroImage = pygame.transform.scale(pygame.image.load('covinv_docs/samus.png'), (70, 90))

rocketHeroImage = pygame.transform.scale(pygame.image.load('covinv_docs/rocket.png'), (70, 90))

invincibleHeroImage = pygame.transform.scale(pygame.image.load('covinv_docs/invincible.png'), (70, 90))

batBossImage = pygame.transform.scale(pygame.image.load('covinv_docs/pngegg.png'),
                                      (200, 140))

bossUSImage = pygame.transform.scale(pygame.image.load('covinv_docs/BossUS.png'),
                                      (200, 200))

angryBossUSImage = pygame.transform.scale(pygame.image.load('covinv_docs/ANGRY BOSS US.png'),
                                      (200, 200))

pangolinImage = pygame.transform.scale(pygame.image.load('covinv_docs/pangolin.png'),
                                      (200, 150))

pangolindefImage = pygame.transform.scale(pygame.image.load('covinv_docs/pangolin_en_boule.png'),
                                      (160, 160))
explosionImage =  pygame.transform.scale(pygame.image.load('covinv_docs/explosion.png'),
                                      (200, 200))

maskImage = pygame.transform.scale(pygame.image.load('covinv_docs/medical-mask.png'), (50, 50))
vaccineImage = pygame.transform.scale(pygame.image.load('covinv_docs/syringe.png'), (50, 50))
bonusAmmoImage = pygame.transform.scale(pygame.image.load('covinv_docs/ammo.png'), (50, 50))
travCertImage = pygame.transform.scale(pygame.image.load('covinv_docs/certification.png'), (50, 50))
freezingImage = pygame.transform.scale(pygame.image.load('covinv_docs/freezing.png'), (40, 40))


startBGImage = pygame.transform.scale(pygame.image.load('covinv_docs/phototest.jpg'),
                                      (WINDOW_WIDTH, WINDOW_HEIGHT))
jungle_BG = pygame.transform.scale(pygame.image.load('covinv_docs/test_BG.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
batcave_BG = pygame.transform.scale(pygame.image.load('covinv_docs/bat_cave.jpeg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
DC_BG = pygame.transform.scale(pygame.image.load('covinv_docs/DC_landscape.jpeg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
whitehouse_BG = pygame.transform.scale(pygame.image.load('covinv_docs/white_house_fire.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
space_BG = pygame.transform.scale(pygame.image.load('covinv_docs/earth.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
spacesun_BG = pygame.transform.scale(pygame.image.load('covinv_docs/sun_pango (2).jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story1_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 1.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story2_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 2.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story3_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 3.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story4_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 4.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story5_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 5.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))
story6_img = pygame.transform.scale(pygame.image.load('covinv_docs/StartBG 6.jpg'),
                                   (WINDOW_WIDTH, WINDOW_HEIGHT))


class Falling:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.falling_img = None

    def draw(self, window):
        window.blit(self.falling_img, (self.x, self.y))

    def update(self):
        pygame.event.pump()

    def move(self, vel):
        self.y += vel

    def touches(self, hero):
        return collide(self, hero)


class Virus(Falling):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = None
        self.virus_img = None

    def draw(self, window):
        window.blit(self.virus_img, (self.x, self.y))


class Bullet:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.random_direction = random.randrange(-8,8,1)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (height >= self.y >= 0)

    def collides_with(self, obj):
        return collide(self, obj)

    def move_pangolin(self, vel):
        self.y += vel
        self.x += self.random_direction
        if self.x <= 0:
            self.random_direction = -self.random_direction
        elif self.x >= 600 - redVirusImage.get_width():
            self.random_direction = -self.random_direction


class Character:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = None
        self.character_img = None
        self.mask = None
        self.bullets = []
        self.bullet_img = None

    # def shoot
    # def move_bullets

    # def draw

    def update(self):
        pygame.event.pump()


class Boss(Character):

    def __init__(self, x, y):
        super(Boss, self).__init__(x, y)
        self.boss_img = batBossImage
        self.mask = pygame.mask.from_surface(self.boss_img)
        self.bullet_img = None
        self.bullets = []
        self.maxhealth = 50
        self.health = 50
        self.random_vel = random.choice([2, -2])

    def draw(self, window):
        window.blit(self.boss_img, (self.x, self.y))
        self.healthbar(window)
        for bullet in self.bullets:
            bullet.draw(window)

    def move_bullets_BossUS(self, vel, hero, invincible):
        for bullet in self.bullets:
            bullet.move(-vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(hero):
                    if not invincible:
                        if hero.lives  > 0:
                            hero.lives -= 1
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

    def move_bullets_pangolin(self, vel, hero, invincible):
        for bullet in self.bullets:
            bullet.move_pangolin(-vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(hero):
                    if not invincible:
                        if hero.lives  >= 0:
                            hero.lives -= 1
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
    def move_bullets_batBoss(self, vel, hero, invincible):
        for bullet in self.bullets:
            bullet.move(-vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(hero):
                    if not invincible:
                        if hero.lives >= 0:
                            hero.lives -= 1
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x + 50, self.y, 100, 8))
        pygame.draw.rect(window, (0, 255, 0), (self.x + 50, self.y, (100) * self.health / self.maxhealth, 8))

    def shoot_BossUS(self):
        boss_ammo = Bullet(random.choice([self.x , self.x + 150]), self.y - 100 + self.boss_img.get_height(), self.bullet_img)
        self.bullets.append(boss_ammo)

    def shoot_Pangolin(self):
        boss_ammo = Bullet(self.x + self.boss_img.get_width()/2 - 40, self.y + 100, self.bullet_img)
        self.bullets.append(boss_ammo)

    def move(self, vel):
        if self.x <= 0:
            self.x += vel
            self.random_vel = vel
        elif 0 < self.x < 100:
            self.x += self.random_vel
        elif self.x == 100:
            self.random_vel = random.choice([vel, -vel])
            self.x += self.random_vel
        elif 100 < self.x < 200:
            self.x += self.random_vel
        elif self.x == 200:
            self.random_vel = random.choice([vel, -vel])
            self.x += self.random_vel
        elif 200 < self.x < 300:
            self.x += self.random_vel
        elif self.x == 300:
            self.random_vel = random.choice([vel, -vel])
            self.x += self.random_vel
        elif 300 < self.x < WINDOW_WIDTH - self.boss_img.get_width():
            self.x += self.random_vel
        elif self.x >= WINDOW_WIDTH - self.boss_img.get_width():
            self.x -= vel
            self.random_vel = -vel


class Hero(Character):

    def __init__(self, x, y):
        super(Hero, self).__init__(x, y)
        self.hero_img = heroImage
        self.mask = pygame.mask.from_surface(self.hero_img)
        self.bullet_img = drop_img
        self.lives = 5
        self.level = 0

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
                    if bullet.collides_with(obj):
                        if obj.health - 1 == 0:
                            objs.remove(obj)
                        else:
                            obj.health -= 1
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    def move_bullets_vs_boss(self, vel, boss, dmg):
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(boss):
                    if boss.boss_img != pangolindefImage:
                        boss.health -= dmg
                    self.bullets.remove(bullet)

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
        "purple": purpleVirusImage,
        "minibat": minibat_img
    }

    Health_Map = {
        "red": HP_RED,
        "green": HP_GREEN,
        "blue": HP_BLUE,
        "purple": HP_PURPLE,
        "minibat": 2
    }


class Bonus(Falling):

    Bonus_List = {
        "mask": maskImage,
        "vaccine": vaccineImage,
        "ammo": bonusAmmoImage,
        "trav_cert": travCertImage,
        "freeze": freezingImage
    }

    def __init__(self, x, y, bonus_num):
        super().__init__(x, y)
        self.bonus_num = bonus_num
        self.bonus_img = self.Bonus_List[bonus_num]
        self.mask = pygame.mask.from_surface(self.bonus_img)

    def draw(self, window):
        window.blit(self.bonus_img, (self.x, self.y))


def collide(obj1, obj2):
    diff_x = int(obj2.x - obj1.x)
    diff_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (diff_x, diff_y)) is not None



def main():
    run = True
    level = 5
    main_font = pygame.font.SysFont("timesnewroman", 20)
    lost_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
    enemies = []
    bonuses = []
    wave_length = 10
    timer_trav_cert = 0
    timer_ammo = 0
    timer_freeze = 0
    timer_mask = 0
    timer_pangolin = 0
    timer_pangolin_def = 0
    wave = 0
    virus_vel = 1
    bonus_vel = 2
    bullet_vel = 5
    boss_vel = 2


    hero = Hero(300, 500)
    batBoss = Boss(200, 0)
    batBoss.bullet_img = batredfire_img
    bossUS = Boss(200, 0)
    bossUS.bullet_img = dynamiteUS_img
    pangolinBoss = Boss(200,0)
    pangolinBoss.bullet_img = pangbat_img

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
        if level % 2 == 1:
            WINDOW.blit(wave_label, (WINDOW_WIDTH / 2 - wave_label.get_width() / 2, 10))

        for enemy in enemies:
            enemy.draw(WINDOW)

        for bonus in bonuses:
            bonus.draw(WINDOW)

        hero.draw(WINDOW)
        if level == 2:
            batBoss.draw(WINDOW)
        if level == 4:
            bossUS.draw(WINDOW)
        if level == 6:
            pangolinBoss.draw(WINDOW)
        pygame.display.update()

    hero_cooldown = 0
    boss_cooldown = 0
    while run:
        hero_cooldown += 1
        clock.tick(FPS)

        if timer_mask <= 0:
            invincible = False
            hero.hero_img = heroImage
        else:
            invincible = True
            timer_mask -= 1
            hero.hero_img = invincibleHeroImage

        if timer_trav_cert <= 0:
            hero_vel = 5
        else:
            hero_vel = 10
            timer_trav_cert -= 1

        if hero.lives <= 0:
            lost = True
            stop()
        if level == 0:
            level = text_screen(level, story1_img, explosionImage, -300, -300)

            pygame.mixer.music.load('covinv_docs/jojo.mp3')
            pygame.mixer.music.play(-1, 0, 0)

        if level == 1:
            BG = jungle_BG
            if len(enemies) == 0:
                wave += 1
                wave_length += 3
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1900, -1700),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -1200),
                                  randBonus)
                    bonuses.append(bonus)
                for i in range(wave_length):
                    randVirus = random.choice(["red", "green"])
                    enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1000, -300),
                                       randVirus,
                                       randVirus)
                    enemies.append(enemy)

            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 500
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 300

            for enemy in enemies[:]:
                if timer_freeze <= 0:
                    enemy.move(virus_vel)
                else:
                    enemy.move(0)
                if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
                    hero.lives -= 1
                    enemies.remove(enemy)
            timer_freeze -= 1
            if wave == 6:
                level = text_screen(level, story2_img, jungle_BG, -300, -300)

                pygame.mixer.music.load('covinv_docs/bowser_mario.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                wave = 0
                wave_length = 10
                enemies = []
                bonuses.clear()
                hero.bullets.clear()
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0

        if level == 2:
            boss_cooldown += 1
            BG = batcave_BG

            if batBoss.health > 25:
                batBoss.move(boss_vel)
                if boss_cooldown % 100 == 0:
                    batBoss.shoot_Pangolin()
                    minibat = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), -100, "minibat", "minibat")
                    enemies.append(minibat)
            else:
                batBoss.bullet_img = batgrnfire_img
                batBoss.move(boss_vel * 2)
                if boss_cooldown % 50 == 0:
                    batBoss.shoot_Pangolin()
                    minibat = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), -100, "minibat", "minibat")
                    enemies.append(minibat)
            if boss_cooldown % 650 == 0:
                randBonus = random.choice(["ammo","trav_cert", "vaccine","mask"])
                bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), -100, randBonus)
                bonuses.append(bonus)
            batBoss.move_bullets_batBoss(-bullet_vel, hero, invincible)
            hero.move_bullets_vs_boss(-bullet_vel, batBoss, 1)

            for minibat in enemies[:]:
                minibat.move(bonus_vel)
                if WINDOW_HEIGHT < 56:
                    enemies.remove(minibat)
                if minibat.touches(hero):
                    if not invincible:
                        hero.lives -= 1
                    enemies.remove(minibat)


            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 300
                    elif bonus.bonus_num == "mask":
                        timer_mask = 400

            if batBoss.health == 0:
                level = text_screen(level, story3_img, BG, batBoss.x, batBoss.y)

                pygame.mixer.music.load('covinv_docs/invaders.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                bossUS.health = 50
                bonuses.clear()
                hero.bullets.clear()
                boss_cooldown = 0
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0
                enemies = []

        if level == 3:
            BG = DC_BG
            if len(enemies) == 0:
                wave += 1
                wave_length += 3
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1900, -1700),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -1200),
                                  randBonus)
                    bonuses.append(bonus)
                for i in range(wave_length):
                    randVirus = random.choice(["red", "green", "blue"])
                    enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1200, -300),
                                       randVirus,
                                       randVirus)
                    enemies.append(enemy)

            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 500
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 300

            for enemy in enemies[:]:
                if timer_freeze <= 0:
                    enemy.move(virus_vel)
                else:
                    enemy.move(0)
                if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
                    hero.lives -= 1
                    enemies.remove(enemy)
            timer_freeze -= 1
            if wave == 6:
                level = text_screen(level, story4_img, BG, -300, -300)

                pygame.mixer.music.load('covinv_docs/brawl.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                wave = 0
                wave_length = 10
                enemies = []
                bonuses.clear()
                hero.bullets.clear()
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0

        if level == 4:
            boss_cooldown += 1
            BG = whitehouse_BG

            if bossUS.health > 25:
                bossUS.boss_img = bossUSImage
                bossUS.move(boss_vel)
                if boss_cooldown % 50 == 0:
                    bossUS.shoot_BossUS()
            else:
                bossUS.boss_img = angryBossUSImage
                bossUS.bullet_img = nukeUS_img
                bossUS.move(boss_vel * 2)
                if boss_cooldown % 25 == 0:
                    bossUS.shoot_BossUS()
            if boss_cooldown % 60 == 0:
                bossUS.y += 1
            if boss_cooldown % 650 == 0:
                randBonus = random.choice(["ammo","trav_cert", "vaccine","mask"])
                bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), -100, randBonus)
                bonuses.append(bonus)
            bossUS.move_bullets_BossUS(-bullet_vel, hero, invincible)
            hero.move_bullets_vs_boss(-bullet_vel, bossUS, 0.5)

            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 300
                    elif bonus.bonus_num == "mask":
                        timer_mask = 400

            if bossUS.health == 0:
                level = text_screen(level, story5_img, BG, bossUS.x, bossUS.y)
                pygame.mixer.music.load('covinv_docs/melee.mp3')
                pygame.mixer.music.play(-1, 0, 0)
                pangolinBoss.health = 50
                bonuses.clear()
                hero.bullets.clear()
                boss_cooldown = 0
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0

        if level == 5:
            BG = space_BG
            hero.hero_img = rocketHeroImage
            if len(enemies) == 0:
                wave += 1
                wave_length += 3
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-2100, -1800),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -1200),
                                  randBonus)
                    bonuses.append(bonus)
                for i in range(wave_length):
                    randVirus = random.choice(["red", "green", "blue", "purple"])
                    enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1500, -300),
                                       randVirus,
                                       randVirus)
                    enemies.append(enemy)

            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 500
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 300

            for enemy in enemies[:]:
                if timer_freeze <= 0:
                    enemy.move(virus_vel)
                else:
                    enemy.move(0)
                if enemy.y + enemy.virus_img.get_height() > WINDOW_HEIGHT - 150:
                    hero.lives -= 1
                    enemies.remove(enemy)
            timer_freeze -= 1
            if wave == 1:
                level, animation = text_screen(level, story6_img, BG, -300, -300)

                pygame.mixer.music.load('covinv_docs/ofortuna.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                wave = 0
                wave_length = 10
                enemies = []
                bonuses.clear()
                hero.bullets.clear()
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0
                if animation:
                    pangolin_arriving()

        if level == 6:
            hero.hero_img = rocketHeroImage
            boss_cooldown += 1
            BG = spacesun_BG


            if timer_pangolin <= 400:
                timer_pangolin += 1
                pangolinBoss.boss_img = pangolinImage
                pangolinBoss.move(boss_vel*2)
                if boss_cooldown % 70 == 0:
                    pangolinBoss.shoot_Pangolin()
            else:
                timer_pangolin_def += 1
                pangolinBoss.boss_img = pangolindefImage
                if boss_cooldown % 30 == 0:
                    pangolinBoss.shoot_Pangolin()
                if timer_pangolin_def == 300:
                    timer_pangolin = 0
                    timer_pangolin_def = 0

            if boss_cooldown % 650 == 0:
                randBonus = random.choice(["ammo","trav_cert", "vaccine","mask"])
                bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), -100, randBonus)
                bonuses.append(bonus)
            pangolinBoss.move_bullets_pangolin(-bullet_vel, hero, invincible)
            hero.move_bullets_vs_boss(-bullet_vel, pangolinBoss, 0.33)

            for bonus in bonuses[:]:
                bonus.move(bonus_vel)
                if bonus.touches(hero) or bonus.y + bonus.bonus_img.get_height() > WINDOW_HEIGHT:
                    bonuses.remove(bonus)
                if bonus.touches(hero):
                    if bonus.bonus_num == "vaccine":
                        hero.lives += 1
                    elif bonus.bonus_num == "trav_cert":
                        timer_trav_cert = 500
                    elif bonus.bonus_num == "ammo":
                        timer_ammo = 300
                    elif bonus.bonus_num == "mask":
                        timer_mask = 400

            if pangolinBoss.health <= 0:
                level = text_screen(level, story2_img, BG, pangolinBoss.x, pangolinBoss.y)
                pygame.mixer.music.load('covinv_docs/ofortuna.mp3')
        if level == 7:
            final_screen()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
                run = False
                quit()  # le quit ici fait que le jeu quitte, sans cela on retourne a l'ecran de depart pour recommencer

        if timer_ammo <= 0:
            if hero_cooldown % 20 == 0:
                hero.shoot()
        else:
            if hero_cooldown % 10 == 0:
                hero.shoot()
                timer_ammo -= 10

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.x - 5 > 0:
            hero.x -= hero_vel
        if keys[pygame.K_RIGHT] and hero.x + 5 + hero.hero_img.get_width() < WINDOW_WIDTH:
            hero.x += hero_vel
        if keys[pygame.K_UP] and hero.y - 5 > 450:
            hero.y -= hero_vel
        if keys[pygame.K_DOWN] and hero.y + 5 + hero.hero_img.get_height() < WINDOW_HEIGHT:
            hero.y += hero_vel

        hero.move_bullets(-bullet_vel, enemies)

        redraw_window()

def  pangolin_arriving():
    timer_pangolin_arriving = 16320
    run = True
    i = -700
    while run:

        WINDOW.blit(spacesun_BG, (0, 0))
        WINDOW.blit(pangolinImage, (200, i))
        WINDOW.blit(rocketHeroImage, (250, 500))
        pygame.display.update()
        timer_pangolin_arriving -= 1
        if i < 0:
            i += 0.05
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if timer_pangolin_arriving <= 0:
            run = False


def text_screen(lvl, image, BG, x, y):
    pygame.init()
    if lvl == 0:
        timer_explosion = 0
    else:
        timer_explosion = 1000
    run = True
    clear_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
    clear_label = clear_font.render("Level clear", 1, (255,255,255))
    mac_font = pygame.font.SysFont("timesnewroman", 20, bold=True)
    mac_label = mac_font.render("Si vous jouez sur un mac, pressez la barre espace", 1, (255, 255, 255))
    while run:
        while timer_explosion > 0:
            WINDOW.blit(BG, (0,0))
            WINDOW.blit(explosionImage, (x,y))
            WINDOW.blit(clear_label, (WINDOW_WIDTH / 2 - clear_label.get_width() / 2, 280))
            pygame.display.update()
            timer_explosion -= 1
        WINDOW.blit(image, (0, 0))
        if lvl == 5:
            WINDOW.blit(mac_label, (WINDOW_WIDTH / 2 - mac_label.get_width() / 2, 450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                elif event.key == K_SPACE:
                    animation = False
                    lvl += 1
                    return  lvl, animation
                else:
                    animation = True
                    lvl += 1
                    return lvl, animation
    pygame.quit()

def final_screen():
    run = True
    final_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
    final_label = final_font.render("BON TRAVAIL ! TU AS MIS FIN A L'INVASION DU COVID", 1, (255, 255, 255))
    continue_label = final_font.render("SI TU VEUX RECOMMENCER APPUIE SUR ESPACE", 1, (255,255,255))
    pygame.mixer.music.stop()
    while run:

        WINDOW.blit(startBGImage, (0, 0))
        WINDOW.blit(final_label, (WINDOW_WIDTH / 2 - final_label.get_width() / 2, 280))
        WINDOW.blit(continue_label, (WINDOW_WIDTH / 2 - continue_label.get_width() / 2, 350))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                elif event.key == K_SPACE:
                    main_start()

    pygame.quit()

def main_start():
    pygame.init()
    run = True
    title_font = pygame.font.SysFont("comicsans", 30)
    pygame.mixer.music.load('covinv_docs/Dior.mp3')
    pygame.mixer.music.play(-1, 0, 0)
    while run:
        WINDOW.blit(startBGImage, (0, 0))
        title_label = title_font.render("Press any key to go to war...", 1, (255, 255, 255))
        WINDOW.blit(title_label, (WINDOW_WIDTH / 2 - title_label.get_width() / 2, 350))
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
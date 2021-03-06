#les imports de base qu'il nous faut pour que notre jeu fonctionne
import pygame
import random
from pygame.locals import *

#initialiser pygame
pygame.font.init()
pygame.mixer.init() # ajouté juste pour etre sur

#on définit les constantes
FPS = 60
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
HP_RED = 1
HP_GREEN = 2
HP_BLUE = 3
HP_PURPLE = 4

#nom de la fenetre de jeu
pygame.display.set_caption("Convinvaders : Revenge of The Pangolin")

#on upload les images qu'on va utiliser, et les sons/musiques

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

herowin = pygame.transform.scale(pygame.image.load('covinv_docs/FrontHero.PNG'), (150, 250))

heroImage = pygame.transform.scale(pygame.image.load('covinv_docs/BackHero.PNG'), (70, 90))

rocketHeroImage = pygame.transform.scale(pygame.image.load('covinv_docs/rocket.png'), (70, 90))

invincibleHeroImage = pygame.transform.scale(pygame.image.load('covinv_docs/Shieldhero.PNG'), (70, 90))

invincibleRocketImage = pygame.transform.scale(pygame.image.load('covinv_docs/rocketshield.png'), (70, 90))


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
explosionImage = pygame.transform.scale(pygame.image.load('covinv_docs/explosion.png'),
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
top1_img = pygame.transform.scale(pygame.image.load('covinv_docs/victory_royale.jpg'),
                                  (WINDOW_WIDTH, WINDOW_HEIGHT))

ahSound = pygame.mixer.Sound('covinv_docs/scream.wav')
waterSound = pygame.mixer.Sound('covinv_docs/water.wav')
victorySound = pygame.mixer.Sound('covinv_docs/lvl_win.wav')
boomSound = pygame.mixer.Sound('covinv_docs/boom.wav')


#classe abstraite regroupant les objets qui tombent du haut de l'écran
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

#classe abstraite Virus, désignant les virus dans leur globalité
class Virus(Falling):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = None
        self.virus_img = None

    def draw(self, window):
        window.blit(self.virus_img, (self.x, self.y))

#classe Bullet qui sert à créer les balles des personnages qui peuvent tirer
class Bullet:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.random_direction = random.randrange(-8, 8, 1)

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


#classe abstraite regroupant tous les personnages du jeu
class Character:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = None
        self.character_img = None
        self.mask = None
        self.bullets = []
        self.bullet_img = None

    def update(self):
        pygame.event.pump()


#classe permettant de modéliser un boss
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

    #trajectoire spécifique des missiles du boss super-infecté
    def move_bullets_BossUS(self, vel, hero, invincible):
        for bullet in self.bullets:
            bullet.move(-vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(hero):
                    if not invincible:
                        if hero.lives > 0:
                            hero.lives -= 1
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

    #trajectoire spécifique des missiles du boss pangoline
    def move_bullets_pangolin(self, vel, hero, invincible):
        for bullet in self.bullets:
            bullet.move_pangolin(-vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                if bullet.collides_with(hero):
                    if not invincible:
                        if hero.lives >= 0:
                            hero.lives -= 1
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

    #trajectoire spécifique des missiles du boss chauve-souris
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

    #fonction modélisant le tir du boss super-infecté
    def shoot_BossUS(self):
        boss_ammo = Bullet(random.choice([self.x, self.x + 150]), self.y - 100 + self.boss_img.get_height(),
                           self.bullet_img)
        self.bullets.append(boss_ammo)

    #fonction modélisant le tir du boss pangolin
    def shoot_Pangolin(self):
        boss_ammo = Bullet(self.x + self.boss_img.get_width() / 2 - 40, self.y + 100, self.bullet_img)
        self.bullets.append(boss_ammo)

    #mouvements des boss
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


#classe permettant de créer notre héros
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

    #fonction modélisant les impacts des balles du héros:
    #soit elles touchent les virus, soit elles disparaissent à la limite de l'écran
    def move_bullets(self, vel, objs):
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(WINDOW_HEIGHT):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collides_with(obj):
                        if obj.health - 1 == 0:
                            waterSound.play()
                            objs.remove(obj)
                        else:
                            obj.health -= 1
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    #fonction modélisant les impacts des balles du héros:
    #soit elles touchent les boss, soit elles disparaissent à la limite de l'écran
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

    #fonction modélisant le tir du héros
    def shoot(self):
        standard_ammo = Bullet(self.x + 23, self.y - 20, self.bullet_img)
        self.bullets.append(standard_ammo)

#classe modélisant les virus, avec une image, une couleur et des points de vie associés à chaque espèce de virus
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

#classe modélisant un bonus, avec une image associée à chaque sorte
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

#fonction permet de détecter une collision d'objets du jeu en détectant les chevauchements de leur masque
def collide(obj1, obj2):
    diff_x = int(obj2.x - obj1.x)
    diff_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (diff_x, diff_y)) is not None

#fonction main, fonction principale qui execute le programme
def main(lvl, vague, hpbat, hpus, hppang):
    run = True
    level = lvl
    animation = False #boolean permettant d'indiquer au programme si il doit lancer l'animation du pangolin au prochain niveau
    main_font = pygame.font.SysFont("timesnewroman", 20)
    lost_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
    enemies = []
    bonuses = []
    wave_length = 10

    #différents timers
    timer_trav_cert = 0
    timer_ammo = 0
    timer_freeze = 0
    timer_mask = 0
    timer_pangolin = 0
    timer_pangolin_def = 0

    wave = vague
    virus_vel = 1
    bonus_vel = 2
    bullet_vel = 5
    boss_vel = 2

    #création des personnages
    hero = Hero(300, 500)
    batBoss = Boss(200, 0)
    batBoss.bullet_img = batredfire_img
    bossUS = Boss(200, 0)
    bossUS.bullet_img = dynamiteUS_img
    pangolinBoss = Boss(200, 0)
    pangolinBoss.bullet_img = pangbat_img

    batBoss.health = hpbat
    bossUS.health = hpus
    pangolinBoss.health = hppang

    clock = pygame.time.Clock()
    lost = False

    #fonction permettant de gérer les cas ou le joueur perd (recommencer le niveau ou quitter)
    def stop(restart):
        lost_label = lost_font.render("Vous avez été infecté", 1, (86, 189, 5))
        lost_label2 = lost_font.render("Vous avez perdu (appuyez sur une touche)", 1, (86, 189, 5))

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
                        level = restart - 1
                        if level == 2:
                            batBoss.health = -1
                            bossUS.health = 50
                            pangolinBoss.health = 50
                        elif level == 4:
                            batBoss.health = -1
                            bossUS.health = -1
                            pangolinBoss.health = 50
                        else:
                            batBoss.health = 50
                            bossUS.health = 50
                            pangolinBoss.health = 50

                        main(level, 6, batBoss.health, bossUS.health, pangolinBoss.health)
            pygame.init()
            pygame.display.update()
            clock.tick(15)

    #fonction qui permet de dessiner en continu les élements nécessaires du jeu à l'écran, au bon moment
    def redraw_window():
        WINDOW.blit(BG, (0, 0))
        if level % 2 == 1:
            pygame.draw.line(WINDOW, (255, 0, 0), (0, 450), (600, 450), 3)  #limite que les virus ne doivent pas franchir
        lives_label = main_font.render(f"Vies: {hero.lives}", 1, (255, 0, 255))
        level_label = main_font.render(f"Niveau: {level}", 1, (255, 255, 255))
        wave_label = main_font.render(f"Vague: {wave}", 1, (255, 255, 255))

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


    #définition et initialisation des cooldown pour le héros et le boss
    hero_cooldown = 0
    boss_cooldown = 0

    while run:
        hero_cooldown += 1
        clock.tick(FPS)

        if timer_mask <= 0:
            invincible = False
            if level < 5:
                hero.hero_img = heroImage
            else:
                hero.hero_img = rocketHeroImage
        else:
            invincible = True
            timer_mask -= 1
            if level == 6:
                hero.hero_img = invincibleRocketImage
            else:
                hero.hero_img = invincibleHeroImage

        if timer_trav_cert <= 0:
            hero_vel = 5
        else:
            hero_vel = 10
            timer_trav_cert -= 1

        if hero.lives <= 0:
            ahSound.play()
            lost = True
            stop(level)
        if level == 0:

            pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
            pygame.mixer.music.play(-1, 10, 0)

            animation = text_screen(level, story1_img, explosionImage, -300, -300)
            level += 1

            pygame.mixer.music.load('covinv_docs/jungle.mp3')
            pygame.mixer.music.play(-1, 115, 0) #commence la musique à 1m55sec directement, assez pratique

            wave = 0
        if level == 1:
            BG = jungle_BG
            if len(enemies) == 0:
                wave += 1
                wave_length += 4
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1900, -1800),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1300, -1200),
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
                        timer_ammo = 300
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 200

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
                victorySound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, story2_img, jungle_BG, -300, -300)
                wave += 1
            if wave == 7:
                level += 1
                pygame.mixer.music.load('covinv_docs/bowser_mario.mp3')
                pygame.mixer.music.play(-1, 0, 0)

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
                randBonus = random.choice(["ammo", "trav_cert", "vaccine", "mask"])
                bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), -100, randBonus)
                bonuses.append(bonus)
            batBoss.move_bullets_batBoss(-bullet_vel, hero, invincible)
            hero.move_bullets_vs_boss(-bullet_vel, batBoss, 0.75)

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
                        timer_mask = 300

            if batBoss.health == -0.25:
                pygame.mixer.music.stop()
                boomSound.play()
                ahSound.play()
                victorySound.play()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3',)
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, story3_img, BG, batBoss.x, batBoss.y)
                batBoss.health = -1
            if batBoss.health == -1:
                level += 1
                pygame.mixer.music.load('covinv_docs/jojo.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                bonuses.clear()
                wave = 0
                wave_length = 10
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
                wave_length += 4
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1900, -1800),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1300, -1200),
                                  randBonus)
                    bonuses.append(bonus)
                for i in range(wave_length):
                    randVirus = random.choice(["red", "green", "blue"])
                    enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -300),
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
                        timer_ammo = 300
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 200

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
                victorySound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, story4_img, BG, -300, -300)
                wave += 1
            if wave == 7:
                level += 1
                pygame.mixer.music.load('covinv_docs/Dragonforce.mp3')
                pygame.mixer.music.play(-1, 0, 0)

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
                if boss_cooldown % 50 == 0: #cooldown du boss, qui est l'intervalle de temps entre chaque tir de missile
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
                randBonus = random.choice(["ammo", "trav_cert", "vaccine", "mask"])
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
                        timer_mask = 300

            if bossUS.health == 0:
                pygame.mixer.music.stop()
                boomSound.play()
                ahSound.play()
                victorySound.play()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, story5_img, BG, bossUS.x, bossUS.y)
                bossUS.health = -1
            if bossUS.health == -1:
                level += 1
                pygame.mixer.music.load('covinv_docs/melee.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                wave = 0
                wave_length = 10
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
            if len(enemies) == 0:
                wave += 1
                wave_length += 3
                if wave < 3:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1700, -1300), randBonus)
                    bonuses.append(bonus)
                else:
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-2100, -2000),
                                  randBonus)
                    bonuses.append(bonus)
                    randBonus = random.choice(["freeze", "vaccine", "trav_cert", "ammo"])
                    bonus = Bonus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -1300),
                                  randBonus)
                    bonuses.append(bonus)
                for i in range(wave_length):
                    randVirus = random.choice(["red", "green", "blue", "purple"])
                    enemy = Colorvirus(random.randrange(50, WINDOW_WIDTH - 100), random.randrange(-1400, -300),
                                       randVirus,randVirus)
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
                        timer_ammo = 300
                    elif bonus.bonus_num == "freeze":
                        timer_freeze = 200

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
                victorySound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, story6_img, BG, -300, -300)
                wave += 1
            if wave == 7:
                level += 1
                pygame.mixer.music.load('covinv_docs/ofortuna.mp3')
                pygame.mixer.music.play(-1, 0, 0)

                enemies = []
                bonuses.clear()
                hero.bullets.clear()
                hero.lives = 5
                timer_trav_cert = 0
                timer_ammo = 0
                timer_freeze = 0
                timer_mask = 0
                if animation: #si le boolean animation est True à ce moment du jeu, cela indique que c'est le moment du niveau final
                    pangolin_arriving()

        if level == 6:
            boss_cooldown += 1
            BG = spacesun_BG
            if timer_pangolin <= 400:
                timer_pangolin += 1
                pangolinBoss.boss_img = pangolinImage
                pangolinBoss.move(boss_vel * 2)
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

            if boss_cooldown % 650 == 0: #intervalle de temps entre les apparitions de bonus, en fonction du cooldown du boss
                randBonus = random.choice(["ammo", "trav_cert", "vaccine", "mask"])
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
                        timer_mask = 300

            if pangolinBoss.health <= 0:
                pygame.mixer.music.stop()
                boomSound.play()
                ahSound.play()
                victorySound.play()
                pygame.mixer.music.load('covinv_docs/txt_screen.mp3')
                pygame.mixer.music.play(-1, 10, 0)
                animation = text_screen(level, top1_img, BG, pangolinBoss.x, pangolinBoss.y)
                level += 1
                pygame.mixer.music.stop()
                victorySound.play()
        if level == 7:
            victorySound.play()
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

        #ce sont les touches à actionner pour faire bouger le héros
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

#fonction implémentée pour l'entrée en scène épique du boss final (pangolin)
def pangolin_arriving():
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

#fonction permettant la gestion des écrans de passage entre niveaux
def text_screen(lvl, image, BG, x, y):
    pygame.init()
    if lvl == 0:
        timer_explosion = 0
    else:
        timer_explosion = 1000
    run = True
    clear_font = pygame.font.SysFont("timesnewroman", 30, bold=True)
    clear_label = clear_font.render("Niveau terminé", 1, (255, 255, 255))
    mac_font = pygame.font.SysFont("timesnewroman", 20, bold=True)
    mac_label = mac_font.render("Si vous jouez sur un mac, pressez la barre espace", 1, (255, 255, 255))

    while run:
        while timer_explosion > 0:
            WINDOW.blit(BG, (0, 0))
            WINDOW.blit(explosionImage, (x, y))
            WINDOW.blit(herowin, (225, 320))
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
                    QUIT
                elif event.key == K_SPACE:
                    animation = False
                    return animation
                elif event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                    pass
                else:
                    animation = True
                    return animation
    pygame.quit()

#fonction qui gère l'écran final du jeu, en cas de victoire du joueur contre le pangolin
def final_screen():
    run = True
    final_font = pygame.font.SysFont("timesnewroman", 20, bold=True)
    final_label = final_font.render("BON TRAVAIL ! TU AS MIS FIN A L'INVASION DU COVID", 1, (255, 255, 255))
    continue_label = final_font.render("SI TU VEUX RECOMMENCER APPUIE SUR ESPACE", 1, (255, 255, 255))
    pygame.mixer.music.stop()
    victorySound.play()
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

#fonction qui appelle le main, faisant office de page de démarrage du jeu
def main_start():
    pygame.init()
    run = True
    title_font = pygame.font.SysFont("comicsans", 30)
    pygame.mixer.music.stop()
    while run:
        WINDOW.blit(startBGImage, (0, 0))
        title_label = title_font.render("Pressez sur une touche...", 1, (255, 255, 255))
        WINDOW.blit(title_label, (WINDOW_WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                else:
                    main(0, 0, 50, 50, 50)
    pygame.quit()


main_start()

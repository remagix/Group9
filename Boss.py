import pygame


class Boss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        pygame.event.pump()

    # points de vie
    # bouger de gauche a droite mais pas se rapprocher de nous
    # tirer des virus
    # l'image utilisée
    # animation quand il prend des degats
    #FAIRE UNE CLASSE MERE ENEMY
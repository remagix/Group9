import pygame


class Virus(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        pygame.event.pump()

        # ATTRIBUTS DUN VIRUS ABSTRAIT
        #taille (depend du virus donc ici on met rien)
        #vitesse (tous la meme , et pour dernier niveau ils accelerent car on est dans fusée donc plus rapide)
        #vitesse quand congelé diminuée pendant 15sec(boolean isFrozen)
        #points d vie (depend de la couleur donc ici on met rien)

        #FAIRE UNE CLASSE ABSTRAITE MERE ENEMY

import pygame
import core
import Graphic
ligne = 30
colonne = 30
taille_jeton = 40

def setup():
    print("bite")
    Graphic.Init_jeux()



def run():

    for i in range(6):
        for y in range(7):
            colonne = taille_jeton+ 10 + y*100
            ligne = taille_jeton + 10 + i*100
            pygame.draw.circle(core.screen, (255, 255, 255), (colonne, ligne), taille_jeton)




core.main(setup, run)
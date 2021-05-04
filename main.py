import pygame
import core
import Graphic
import Objet

blanc = [255, 255, 255]
ligne = 0
colonne = 0
taille_jeton = 40

Joueur1 = Objet.Joueur()
Joueur2 = Objet.Joueur()

def setup():

    Graphic.Init_jeux(taille_jeton)


    Joueur1.couleur = [255,0,0]
    Joueur2.couleur = [255, 215, 0]
def run():
    print("coucou")
    Objet.Grille.miseEnPlace(self=0)




core.main(setup, run)
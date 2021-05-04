import pygame
import core
import Graphic
import Objet

blanc = [255, 255, 255]
ligne = 0
colonne = 0
taille_jeton = 40

Joueur1 = Objet
Joueur2 = Objet.Joueur()

def setup():

    Joueur1.couleur = [255,0,0]
    Joueur2.couleur = [255, 215, 0]


def run():
    print(Joueur1.Get_Nom())
    Joueur1.Set_Nom("Yassin")
    print(Joueur1.Get_Nom())



core.main(setup, run)
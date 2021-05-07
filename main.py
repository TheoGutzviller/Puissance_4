import pygame
import core
import Graphic
import Objet
import Variable

ligne = 0
colonne = 0
taille_jeton = 40

Joueur1 = Objet.Joueur()
Joueur2 = Objet.Joueur()
Fenetre = Graphic.GUI()


def setup():

    core.WINDOW_SIZE = Variable.Taille_fenetre
    Joueur1.couleur = [255, 0, 0]
    Joueur2.couleur = [255, 215, 0]


def run():
    print(Joueur1.Get_Nom())
    Joueur1.Set_Nom("Yassin")
    print(Joueur1.Get_Nom())

    Fenetre.Mise_en_Place_Pions()



core.main(setup, run)

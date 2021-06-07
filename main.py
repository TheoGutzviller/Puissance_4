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
list_cases=[]
pions_rouge=Objet.Pions
pions_jaune=Objet.Pions

pions_jaune.Set_Case(Variable.jaune)
pions_rouge.Set_Case(Variable.rouge)

def setup():
    global Info,Variable
    core.WINDOW_SIZE = Variable.Taille_fenetre

    Joueur1.couleur = Variable.rouge
    Joueur2.couleur = Variable.jaune


    print("quel est le nom de joueur 1 ?")

    Joueur1.Set_Nom(input())
    print("quel est le nom de joueur 2 ?")

    Joueur2.Set_Nom(input())

    for i in range(42):
        list_cases.append(Objet.Case)


def run():
    global Info

    Fenetre.Mise_en_Place_Pions()


    for w in range(22):
        print("tkt")


    if w==21:
        while True:
            print("kodso")




core.main(setup, run)

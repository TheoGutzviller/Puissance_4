import pygame as pg
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
pions_rouge=Objet.Pions()
pions_jaune=Objet.Pions()

pions_jaune.Set_Case(Variable.jaune)
pions_rouge.Set_Case(Variable.rouge)


def setup():
    global Info,Variable
    core.WINDOW_SIZE = Variable.Taille_fenetre

    Joueur1.Set_Couleur(Variable.rouge)
    Joueur2.Set_Couleur(Variable.jaune)


    print("quel est le nom de joueur 1 ?")

    #Joueur1.Set_Nom(input())
    print("quel est le nom de joueur 2 ?")

    #Joueur2.Set_Nom(input())

    for i in range(42):
        list_cases.append(Objet.Case())



def run():
    global Info
    temp=0

    for w in range(42):
            list_cases[w].Set_Couleur(Variable.blanc)

    #for partie in range(24):

        #list_cases[41].Set_Couleur(Variable.jaune)
    if temp == 0:
            colonne= ((6-1) + (5*7))

            Fenetre.Mise_en_Place_Pions()

            print(list_cases[colonne].Get_Couleur())
            if ((list_cases[colonne].Get_Couleur() != Variable.blanc)):
                while ((list_cases[colonne].Get_Couleur() != Variable.blanc)&(colonne>7)):
                    colonne = colonne - 7
                    list_cases[colonne+7].Set_Couleur(Variable.blanc)
            else :
                print("coucou")

            #print(colonne)
            list_cases[colonne].Set_Couleur(Joueur1.Get_Couleur())  #couleur joueur1 = rouge
            #list_cases[colonne].Set_Couleur((125,90,47))
            #print(colonne)
            for i in range(6):
                for y in range(7):
                    var = 0
                    var = y + i*7
                    #print(var)
                    pg.draw.circle(core.screen, list_cases[var].Get_Couleur(), (
                        ((Variable.Taille_pions + 10) + (y * (Variable.Taille_pions * 2 + 10))),
                        ((Variable.Taille_pions + 10) + (i * (Variable.Taille_pions * 2 + 10)))), Variable.Taille_pions)


core.main(setup, run)

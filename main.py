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
Partie = Objet.Partie()

pions_jaune.Set_Case(Variable.jaune)
pions_rouge.Set_Case(Variable.rouge)


def setup():
    global Info,Variable
    core.WINDOW_SIZE = Variable.Taille_fenetre

    Joueur1.Set_Couleur(Variable.rouge)
    Joueur2.Set_Couleur(Variable.jaune)




    for i in range(42):
        list_cases.append(Objet.Case())
        list_cases[i].Set_Couleur(Variable.blanc)


def run():
    global Info
    temp=0
    entrée= 0
    Partie.nb_manche += 1


    while True :
        entrée= int(input())
        if ((entrée<8)&(entrée>0)):
            print(list_cases[entrée-1].Get_Couleur())
            if((list_cases[entrée-1].Get_Couleur() == Variable.blanc)):
                colonne = ((entrée - 1) + (5 * 7))
                break


    if ((list_cases[colonne].Get_Couleur() != Variable.blanc)):
        while ((list_cases[colonne].Get_Couleur() != Variable.blanc)&(colonne>6)):
            colonne = colonne - 7
            #list_cases[colonne+7].Set_Couleur(Variable.blanc)

    if Partie.nb_manche%2:
        list_cases[colonne].Set_Couleur(Joueur1.Get_Couleur())
    else :
        list_cases[colonne].Set_Couleur(Joueur2.Get_Couleur())
        #print(colonne)
    for i in range(6):
        for y in range(7):
            var = 0
            var = y + i*7
            #print(var)
            pg.draw.circle(core.screen, list_cases[var].Get_Couleur(), (
                ((Variable.Taille_pions + 10) + (y * (Variable.Taille_pions * 2 + 10))),
                ((Variable.Taille_pions + 10) + (i * (Variable.Taille_pions * 2 + 10)))), Variable.Taille_pions)

    if(Partie.nb_manche==42): #la partie s'arrete si l'un des 2 joueurs a gagné ou que ne nombre de manche a atteint le maximum
        if((Joueur1.Get_Score()==10)|(Joueur2.Get_Score()==10)):
            while True :
                print("partie fini !!!!!! ")
        else:
            while True:
                print("partie fini !!!!!! ")
core.main(setup, run)

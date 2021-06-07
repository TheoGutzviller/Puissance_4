import pygame
import Variable


class Joueur:
    nom = "Kevin <3"
    score = 0
    couleur = [255, 255, 255]

    def Get_Nom(self):
        return Joueur.nom

    def Set_Nom(self, Nom):
        Joueur.nom = Nom

    def Get_Score(self):
        return Joueur.score

    def Get_Couleur(self):
        return Joueur.couleur

    def Set_Couleur(self, Couleur):
        Joueur.Couleur = Couleur


class Pions:
    global blanc
    Couleur = Variable.couleur
    Taille_pions = 40
    case = [0,0]

    def Get_Case(self):
        return Pions.Couleur

    def Set_Case(self,couleur=[0,0,0]):
        Pions.Couleur = couleur


class Grille:
    global core
    pions = []

    def miseEnPlace(self, taille_jeton):
        colonne = 0
        ligne = 0

        for i in range(6):
            for y in range(7):
                colonne = taille_jeton + 20 + y * 120
                ligne = taille_jeton + 100 + i * 120

                pygame.draw.circle(core.screen, blanc, (colonne, ligne), taille_jeton)


class Case:

    Couleur = Variable.couleur

    def CaseVide(self):
        print("vide")

    def Contenu(self):
        if (Variable.blanc == couleur) :
            print("vide")
        else:
            print("plein")




class Partie:


    def MiseEnPlace(self):
        Joueur_1 = Joueur
        Joueur_2 = Joueur

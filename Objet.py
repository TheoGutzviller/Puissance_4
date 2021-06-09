import pygame
import Variable


class Joueur:
    nom = "Kevin <3"
    score = 0
    Couleur = [255, 255, 255]

    def Get_Nom(self):
        return Joueur.nom

    def Set_Nom(self, Nom):
        self.nom = Nom

    def Get_Score(self):
        return self.score

    def Get_Couleur(self):
        return self.Couleur

    def Set_Couleur(self, Couleur):
        self.Couleur = Couleur


class Pions:
    global blanc
    Couleur = Variable.couleur
    Taille_pions = 40
    case = [0,0]

    def Get_Case(self):
        return Pions.Couleur

    def Set_Case(self,couleur=[0,0,0]):
        self.Couleur = couleur


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

                pg.draw.circle(core.screen, blanc, (colonne, ligne), taille_jeton)


class Case:

    Couleur = Variable.blanc

    def Case_Vide(self):
        print("vide")

    def Contenu(self):
        if (Variable.blanc == couleur) :
            print("vide")
        else:
            print("plein")

    def Get_Couleur(self):
        return self.Couleur

    def Set_Couleur(self,couleur=[0,0,0]):
        self.Couleur = couleur




class Partie:


    def MiseEnPlace(self):
        Joueur_1 = Joueur()
        Joueur_2 = Joueur()

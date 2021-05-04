class Joueur:
    nom = ""
    score = 0
    couleur = [255,255,255]

    def get_nom(self):
         print("coucou")
    #methods get_nom / set_Nom


class Grille:
    def miseEnPlace(taille_jeton):
        colonne = 0
        ligne = 0

        for i in range(6):
            for y in range(7):
                colonne = taille_jeton + 20 + y * 120
                ligne = taille_jeton + 100 + i * 120

                pygame.draw.circle(core.screen, blanc, (colonne, ligne), taille_jeton)

class pions:
    print("coucou")

class emplacement:
    print("coucou")

class partie:
    print("coucou")


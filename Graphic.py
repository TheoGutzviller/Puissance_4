import core
import pygame
import Variable
import Objet



class GUI:


    def Affich_pos_pions(self):
        print("jvfhku")

    def Affich_score(self):
        print("jvfhku")

    def Mise_en_Place_Pions(self):
        print("jdsnsonqs")
        for i in range (7):
            for y in range (6):
                pygame.draw.circle(core.screen, Variable.blanc, ((Variable.Taille_pions+10)+(i*(Variable.Taille_pions*2+10)), (Variable.Taille_pions+10)+(y*(Variable.Taille_pions*2+10))), Variable.Taille_pions)
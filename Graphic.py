import core
import pygame as pg
import Variable
import Objet
import TexteInput


class GUI:
    global list_cases
    chaine_carac = ["", ""]
    def Affich_pos_pions(self):
        print("mdr")
        i=0
        y=0
        pg.draw.circle(core.screen, list_cases[0].couleur, (
        ((Variable.Taille_pions + 10) + (i * (Variable.Taille_pions * 2 + 10))),
        ((Variable.Taille_pions + 10) + (y * (Variable.Taille_pions * 2 + 10)))), Variable.Taille_pions)


    def Affich_score(self):
        print("jvfhku")

    def Mise_en_Place_Pions(self):
        for i in range(6):
            for y in range(7):

                pg.draw.circle(core.screen, Variable.couleur, (((Variable.Taille_pions + 10) + (y * (Variable.Taille_pions * 2 + 10))),((Variable.Taille_pions + 10) + (i * (Variable.Taille_pions * 2 + 10)))), Variable.Taille_pions)

    def InfoBox(self, screen):
        clock = pg.time.Clock()
        input_box2 = TexteInput.InputBox(400, 700, 140, 32)
        input_box1 = TexteInput.InputBox(50, 700, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        val = ""

        while not done:

            for event in pg.event.get():
                if event.type == pg.QUIT: # a controler pr quitter fenetre
                    done = True
                for box in input_boxes:
                    box.handle_event(event)
                    #GUI.chaine_carac[0] = input_box1.carac
                   #GUI.chaine_carac[1] = input_box2.carac
                    #if ((GUI.chaine_carac[0]!="") | (GUI.chaine_carac[1]!="")):
                        #print(GUI.chaine_carac[0])
                        #print(GUI.chaine_carac[1])






            for box in input_boxes:
                box.update()


            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)

            pg.display.flip()
            clock.tick(30)

        return [x.text for x in input_boxes]

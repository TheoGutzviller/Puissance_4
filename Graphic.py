import core
import pygame as pg
import Variable
import Objet
import TexteInput



class GUI:


    def Affich_pos_pions(self):
        print("jvfhku")

    def Affich_score(self):
        print("jvfhku")

    def Mise_en_Place_Pions(self):
        print("jdsnsonqs")
        for i in range (7):
            for y in range (6):
                pg.draw.circle(core.screen, Variable.blanc, ((Variable.Taille_pions+10)+(i*(Variable.Taille_pions*2+10)), (Variable.Taille_pions+10)+(y*(Variable.Taille_pions*2+10))), Variable.Taille_pions)

    def InfoBox(self):
        global screen
        clock = pg.time.Clock()
        input_box1 = TexteInput.InputBox(600, 700, 140, 32)
        input_box2 = TexteInput.InputBox(100, 700, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)

            pg.display.flip()
            clock.tick(30)




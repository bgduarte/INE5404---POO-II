import sys
import pygame
from events import Events


class EventsJogando(Events):
    def __init__(self,player):
        self.__player = player
        self.__pausa = False
        self.__mouseClick = False

    @property
    def pausa(self):
        return self.__pausa
        
    @pausa.setter
    def pausa(self, pausa):
        self.__pausa = pausa

    @property
    def mouseClick(self):
        return self.__mouseClick

    def check_events(self):
        self.__pausa = False
        self.__mouseClick = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keyup events
            if event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_a) or 
                   (event.key == pygame.K_LEFT)):
                    self.__player.move_left()

                elif ((event.key == pygame.K_d) or 
                     (event.key == pygame.K_RIGHT)):
                    self.__player.move_right()

                elif (event.key == pygame.K_p):
                    self.__pausa = True
                elif (event.key == pygame.K_p):
                    self.__pausa = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseClick = True
            else:
                self.__mouseClick = False

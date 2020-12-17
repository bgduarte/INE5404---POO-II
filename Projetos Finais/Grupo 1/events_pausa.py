import pygame
from events import Events
import sys


class EventsPausa(Events):
    def __init__(self):
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
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_p):
                    self.__pausa = True
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseClick = True
            else:
                self.__mouseClick = False

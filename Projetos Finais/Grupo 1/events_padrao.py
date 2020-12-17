import sys
import pygame
from events import Events


class EventsPadrao(Events):
    def __init__(self):
        self.__mouseClick = False

    @property
    def mouseClick(self):
        return self.__mouseClick

    def check_events(self):
        self.__mouseClick = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseClick = True
            else:
                self.__mouseClick = False

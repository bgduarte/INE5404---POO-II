import sys
import pygame
from events_padrao import EventsPadrao


class EventsDerrota(EventsPadrao):
    def __init__(self, textbox):
        self.__mouseClick = False
        self.__textbox = textbox

    @property
    def mouseClick(self):
        return self.__mouseClick

    @property
    def textbox(self):
        return self.__textbox

    @textbox.setter
    def textbox(self, textbox):
        self.__textbox = textbox

    @property
    def events(self):
        return pygame.event.get()

    def check_events(self):
        self.__mouseClick = False
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseClick = True
            else:
                self.__mouseClick = False

        self.__textbox.listen(events)

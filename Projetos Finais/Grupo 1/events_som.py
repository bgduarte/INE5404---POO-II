import sys
import pygame
from events import Events


class EventsSom(Events):
    def __init__(self, sliders):
        self.__mouseClick = False
        self.__sliders = sliders

    @property
    def mouseClick(self):
        return self.__mouseClick

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

        for slider in self.__sliders:
            slider.listen(events)

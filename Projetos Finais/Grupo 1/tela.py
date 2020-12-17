import pygame
from singleton import Singleton


class Tela(metaclass=Singleton):
    def __init__(self):
        self.__medidas = (400,600)
        self.__display = pygame.display.set_mode(self.__medidas)

    @property
    def display(self):
        return self.__display

    @property
    def width(self):
        return self.__display.get_width()

    @property
    def height(self):
        return self.__display.get_height()

    def update(self):
        pygame.display.update()

    def fill(self, cor):
        self.__display.fill(cor)

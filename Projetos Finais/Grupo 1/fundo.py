import pygame
from tela import Tela

class Fundo:

    def __init__(self, param, cor):
        
        #Parametros = (left, top, width, height)
        self.__param = param
        self.__cor = cor
        self.__tela = Tela()

        self.__rect = pygame.Rect(*self.__param)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        self.__param = param
        self.__rect = pygame.Rect(*self.__param)

    @property
    def rect(self):
        return self.__rect     

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def tela(self):
        return self.__tela

    def update_width(self, qtd):
        if self.__rect.x < self.__tela.width:
            self.__rect.x -= qtd
            self.__rect.width += qtd

    def blitme(self):
        pygame.draw.rect(self.__tela.display, self.__cor, self.__rect, 0, 10)
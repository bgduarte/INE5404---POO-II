from texto import Texto
from fundo import Fundo
import pygame


class Botao:
    def __init__(self,
                 texto: Texto,
                 fundo: Fundo,
                 cor_normal: tuple,
                 cor_mouse: tuple,
                 eventos: object):
        self.__texto = texto
        self.__fundo = fundo
        self.__cor_normal = cor_normal
        self.__cor_mouse = cor_mouse
        self.__eventos = eventos

    def update(self):
        mouse = pygame.mouse.get_pos()
        if ((self.__fundo.rect.x + self.__fundo.rect.width > mouse[0] > self.__fundo.rect.x) and
            (self.__fundo.rect.y + self.__fundo.rect.height > mouse[1] > self.__fundo.rect.y)):

            self.__fundo.cor = self.__cor_mouse

            if self.__eventos.mouseClick:
                return True

        else:
            self.__fundo.cor = self.__cor_normal
        return False

    def draw(self):
        self.__fundo.blitme()
        self.__texto.draw()

    @property
    def texto(self):
        return self.__texto

    @property
    def fundo(self):
        return self.__fundo

    @property
    def cor_normal(self):
        return self.__cor_normal

    @property
    def cor_mouse(self):
        return self.__cor_mouse

    @property
    def eventos(self):
        return self.__eventos

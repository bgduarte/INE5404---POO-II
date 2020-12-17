import pygame
from tela import Tela


class Texto:
    def __init__(self,
                 texto,
                 font,
                 tamanho,
                 cor,
                 posicao):
    
        self.__texto = texto
        self.__font = font
        self.__tamanho = tamanho
        self.__cor = cor
        self.__tela = Tela()
        self.__posicao = posicao

        self.__fonteCompleta = pygame.font.Font(self.__font, self.__tamanho)

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    def draw(self):
        temp = self.__fonteCompleta.render(self.__texto, False, self.__cor).convert_alpha(self.__tela.display)
        self.__tela.display.blit(temp, self.__posicao)


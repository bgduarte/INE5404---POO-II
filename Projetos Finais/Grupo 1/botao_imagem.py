from fundo import Fundo
from botao import Botao
from tela import Tela
import pygame


class BotaoImagem(Botao):
    def __init__(self,
                 sprite: pygame.sprite.Sprite,
                 posicao: tuple,
                 fundo: Fundo,
                 cor_normal: tuple,
                 cor_mouse: tuple,
                 eventos: object):
        super().__init__("", fundo, cor_normal, cor_mouse, eventos)
        self.__sprite = sprite
        self.__tela = Tela()
        self.__posicao = posicao

    def draw(self):
        self.fundo.blitme()
        self.__tela.display.blit(self.__sprite, self.__posicao)

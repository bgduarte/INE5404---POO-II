from fase import Fase
from tela import Tela
from bg_element import BGElement
from pontuacao_controller import PontuacaoController
import pygame


class FasesController:
    def __init__(self):
        self.__pontuacao = PontuacaoController()
        self.__tela = Tela()
        
        # Fase 1
        self.__bg_1 = pygame.image.load("Materials/AnimatedStreet.png").convert(self.__tela.display)
        self.__linha_img = pygame.image.load("Materials/AnimatedStreet_Element.png").convert(self.__tela.display)
        self.__linha1 = BGElement([115, -53], [self.__linha_img])
        self.__linha2 = BGElement([230, -53], [self.__linha_img])
        self.__linha3 = BGElement([115, 292], [self.__linha_img])
        self.__linha4 = BGElement([230, 292], [self.__linha_img])
        self.__fase1 = Fase(self.__bg_1, [self.__linha1, self.__linha2, self.__linha3, self.__linha4])
        
        self.__fases = [self.__fase1]
        self.__fase = 0
        self.__fase_atual = self.__fases[self.__fase]

    def update(self):
        if len(self.__fases) > 1 and self.__pontuacao.pontos % 1000 == 0 and self.__pontuacao.pontos > 0:
            if self.__fase == len(self.__fases) - 1:
                self.__fase = 0
            else:
                self.__fase += 1
        self.__fase_atual = self.__fases[self.__fase]

    def zerar(self):
        self.__fase = 0

    @property
    def fase_atual(self):
        return self.__fase_atual

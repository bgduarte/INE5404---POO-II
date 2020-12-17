from efeito import Efeito
from tela import Tela
from pontuacao_controller import PontuacaoController
import pygame


class AlcoolGel(Efeito):
    def __init__(self, posicao):
        self.__tela = Tela()
        super().__init__(posicao, [pygame.image.load("Materials/alcool gel.png").convert_alpha(self.__tela.display)])
        self.__pontuacao_controller = PontuacaoController()
        self.img_atual = self.anim[0]
        self.rect = self.img_atual.get_rect()
        self.pos_inicial()
        self.__ativo = False

    def update(self):
        self.rect.y += self.velocidade_controller.vel_atual
        if (self.rect.top >= self.tela.height):
            self.kill()

    def efeito(self):
        super().efeito()
        if not self.__pontuacao_controller.multiplicador_ativo:
            self.__pontuacao_controller.multiplicador_ativo = True
            self.__pontuacao_controller.multiplicador = 2
        else:
            self.__pontuacao_controller.timer_multiplicador = 0
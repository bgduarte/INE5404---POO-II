from efeito import Efeito
from tela import Tela
import pygame


class Mascara(Efeito):
    def __init__(self, posicao, jogador):
        self.__tela = Tela()
        super().__init__(posicao, [pygame.image.load("Materials/mascara.png").convert_alpha(self.__tela.display)])
        self.__jogador = jogador
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
        if not self.__jogador.invencivel:
            self.__jogador.invencivel = True
        else:
            self.__jogador.timer_invencivel = 0

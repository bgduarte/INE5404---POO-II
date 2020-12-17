from efeito import Efeito
from tela import Tela
import pygame


class Vacina(Efeito):
    def __init__(self, posicao, jogador):
        self.__tela = Tela()
        super().__init__(posicao, [pygame.image.load("Materials/vacina.png").convert_alpha(self.__tela.display)])
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
        self.__jogador.ganha_vida()

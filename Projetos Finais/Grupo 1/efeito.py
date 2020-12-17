from objeto import Objeto
from abc import ABC, abstractmethod
from pontuacao_controller import PontuacaoController

class Efeito(Objeto, ABC):
    def __init__(self, posicao, imagem):
        super().__init__(posicao, imagem)
        self.img_atual = self.anim[0]
        self.rect = self.img_atual.get_rect()
        self.pos_inicial()
        self.spriteNum = 0
        self.spriteNumMax = len(self.anim)
        self.spriteTimer = 0
        self.spriteTimerMax = 4
        self.__pontuacao_controller = PontuacaoController()

    def update(self):
        self.rect.y += self.velocidade_controller.vel_atual
        if (self.rect.top >= self.tela.height):
            self.kill()
        self.efeito()

    @abstractmethod
    def efeito(self):
        self.__pontuacao_controller.pontos += 100

    @property
    def pontuacao_controller(self):
        return self.__pontuacao_controller
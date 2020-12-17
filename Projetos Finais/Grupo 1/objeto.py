from abc import ABC, abstractmethod
import pygame
from tela import Tela
from velocidade_controller import VelocidadeController


class Objeto(pygame.sprite.Sprite, ABC):
    def __init__(self,
                 posicao: list,
                 anim: list):
        super().__init__()
        self.__posicao = posicao
        self.__tela = Tela()
        self.__anim = anim
        self.__velocidade_controller = VelocidadeController()
        #Vão ser implementados nas subclasses
        self.__img_atual = None
        self.__spriteNum = 0
        self.__spriteNumMax = 0
        self.__spriteTimer = 0
        self.__spriteTimerMax = 0
        #Colocar isso no init das subclasses
        # self.pos_inicial()

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def tela(self):
        return self.__tela

    @property
    def img_atual(self):
        return self.__img_atual

    @img_atual.setter
    def img_atual(self, img):
        self.__img_atual = img

    @property
    def anim(self):
        return self.__anim

    @anim.setter
    def anim(self, anim):
        self.__anim = anim

    @property
    def spriteNum(self):
        return self.__spriteNum

    @spriteNum.setter
    def spriteNum(self, spriteNum):
        self.__spriteNum = spriteNum

    @property
    def spriteNumMax(self):
        return self.__spriteNumMax

    @spriteNumMax.setter
    def spriteNumMax(self, spriteNumMax):
        self.__spriteNumMax = spriteNumMax

    @property
    def spriteTimer(self):
        return self.__spriteTimer

    @spriteTimer.setter
    def spriteTimer(self, spriteTimer):
        self.__spriteTimer = spriteTimer

    @property
    def spriteTimerMax(self):
        return self.__spriteTimerMax

    @spriteTimerMax.setter
    def spriteTimerMax(self, spriteTimerMax):
        self.__spriteTimerMax = spriteTimerMax

    @property
    def velocidade_controller(self):
        return self.__velocidade_controller

    def pos_inicial(self):
        if len(self.__posicao) >= 2:
            self.rect.x = self.__posicao[0]
            self.rect.y = self.__posicao[1]
        else:
            self.rect.x = 0
            self.rect.y = 0

    def animacao(self):
        self.__spriteTimer +=1
        if self.__spriteTimer>=self.__spriteTimerMax:
            self.__spriteNum +=1
            self.__spriteTimer = 0

        if self.__spriteNum >= self.__spriteNumMax:
            self.__spriteNum = 0

        self.img_atual = self.__anim[self.__spriteNum]

    def blitme(self):
        self.tela.display.blit(self.__img_atual, self.rect)

    @abstractmethod
    def update(self):
        pass

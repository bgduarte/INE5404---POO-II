from abc import ABC, abstractmethod
from velocidade_controller import VelocidadeController
from som_controller import SomController
from tela import Tela
import pygame
import random


class ObjetosController(ABC):
    def __init__(self, jogador):
        self.__tela = Tela()
        self.__jogador = jogador
        self.__timer_max = 30
        self.__timer = 0
        self.__velocidade_controller = VelocidadeController()
        self.__som_controller = SomController()
        self.__limite_vel = 10
        self.__pista1 = pygame.sprite.Group()
        self.__pista2 = pygame.sprite.Group()
        self.__pista3 = pygame.sprite.Group()
        self.__pistas = [self.__pista1, self.__pista2, self.__pista3]
        
        
    @property
    def tela(self):
        return self.__tela

    @property
    def jogador(self):
        return self.__jogador

    @property
    def timer_max(self):
        return self.__timer_max

    @timer_max.setter
    def timer_max(self, timer_max):
        self.__timer_max = timer_max

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    @property
    def limite_vel(self):
        return self.__limite_vel

    @limite_vel.setter
    def limite_vel(self, limite_vel):
        self.__limite_vel = limite_vel

    @property
    def velocidade_controller(self):
        return self.__velocidade_controller

    @property
    def som_controller(self):
        return self.__som_controller

    @property
    def pista1(self):
        return self.__pista1

    @property
    def pista2(self):
        return self.__pista2

    @property
    def pista3(self):
        return self.__pista3

    @property
    def pistas(self):
        return self.__pistas

    @abstractmethod
    def cria_objeto(self, qtd):
        pass
                    
    @abstractmethod
    def timer_update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def check_colisao(self):
        pass

    def zerar(self):
        self.__timer_max = 30
        self.__timer = 0
        for pista in self.pistas:
            pista.empty()

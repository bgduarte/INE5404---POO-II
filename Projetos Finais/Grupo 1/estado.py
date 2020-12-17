from abc import ABC, abstractmethod
from tela import Tela
from pontuacao_controller import PontuacaoController
from som_controller import SomController
from velocidade_controller import VelocidadeController
from fases_controller import FasesController
from recordes_controller import RecordesController
from jogador import Jogador
import pygame


class Estado(ABC):
    def __init__(self, jogador=None, obstaculo_controller=None, efeito_controller=None):
        self.__jogador = jogador
        self.__tela = Tela()
        self.__pontuacao = PontuacaoController()
        self.__som_controller = SomController()
        self.__velocidade_controller = VelocidadeController()
        self.__obstaculo_controller = obstaculo_controller
        self.__efeito_controller = efeito_controller
        self.__fases_controller = FasesController()
        self.__recordes_controller = RecordesController()
        self.__GREEN = (0, 100, 0)
        self.__DARK_GREEN = (0, 80, 0)
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)
        self.__GREY = (100, 100, 100)
        self.__DARK_GREY = (70, 70, 70)
        self.__YELLOW = (220, 220, 0)
        self.__SILVER = (160, 160, 160)
        self.__BRONZE = (150, 100, 0)
        self.__musica = False

    @property
    def musica(self):
        return self.__musica

    @musica.setter
    def musica(self, musica):
        self.__musica = musica

    @property
    def jogador(self):
        return self.__jogador

    @property
    def tela(self):
        return self.__tela

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def som_controller(self):
        return self.__som_controller

    @property
    def velocidade_controller(self):
        return self.__velocidade_controller

    @property
    def obstaculo_controller(self):
        return self.__obstaculo_controller

    @property
    def efeito_controller(self):
        return self.__efeito_controller

    @property
    def fases_controller(self):
        return self.__fases_controller

    @property
    def recordes_controller(self):
        return self.__recordes_controller

    @property
    def BLACK(self):
        return self.__BLACK

    @property
    def WHITE(self):
        return self.__WHITE

    @property
    def GREEN(self):
        return self.__GREEN

    @property
    def DARK_GREEN(self):
        return self.__DARK_GREEN

    @property
    def GREY(self):
        return self.__GREY

    @property
    def DARK_GREY(self):
        return self.__DARK_GREY

    @property
    def YELLOW(self):
        return self.__YELLOW

    @property
    def SILVER(self):
        return self.__SILVER
    
    @property
    def BRONZE(self):
        return self.__BRONZE

    @abstractmethod
    def start(self):
        pass

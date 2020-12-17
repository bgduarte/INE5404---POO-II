from texto import Texto
from tela import Tela
from fundo import Fundo
from velocidade_controller import VelocidadeController
from singleton import Singleton


class PontuacaoController(metaclass=Singleton):
    def __init__(self):
        self.__pontos = 0
        self.__tela = Tela()
        self.__WHITE = (255, 255, 255)
        self.__GREEN = (0, 100, 0)
        self.__texto = Texto("", "Materials/Early GameBoy.ttf", 25, self.__WHITE, [370, 10])

        self.__timer = 0
        self.__timerMax = 30
        self.__timerAtual = self.__timerMax
        self.__velocidade_controller = VelocidadeController()
        self.__len_pontuacao = 1
        self.__fundo = Fundo([360, 10, 35, 30], self.__GREEN)

        self.__multiplicador = 1
        self.__multiplicador_ativo = False
        self.__timer_multiplicador = 0
        self.__timer_multiplicador_max = 300

    @property
    def multiplicador(self):
        return self.__multiplicador

    @multiplicador.setter
    def multiplicador(self, multiplicador):
        self.__multiplicador = multiplicador

    @property
    def multiplicador_ativo(self):
        return self.__multiplicador_ativo

    @multiplicador_ativo.setter
    def multiplicador_ativo(self, multiplicador_ativo):
        self.__multiplicador_ativo = multiplicador_ativo

    @property
    def timer_multiplicador(self):
        return self.__timer_multiplicador

    @timer_multiplicador.setter
    def timer_multiplicador(self, timer_multiplicador):
        self.__timer_multiplicador = timer_multiplicador

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @property
    def fundo(self):
        return self.__fundo

    def draw(self):
        self.__texto.texto = str(self.__pontos)
        self.__texto.draw()

    def update(self):
        if self.__multiplicador_ativo:
            self.__timer_multiplicador += 1
            if self.__timer_multiplicador >= self.__timer_multiplicador_max:
                self.__timer_multiplicador = 0
                self.__multiplicador_ativo = False
                self.__multiplicador = 1

        self.__timerAtual = self.__timerMax / self.__velocidade_controller.vel_atual
        self.__timer += 1
        if self.__timer > self.__timerAtual:
            self.__timer = 0
            self.__pontos += 1 * self.__multiplicador
        self.ajuste_pontos()

    def ajuste_pontos(self):
        if self.__len_pontuacao < len(str(self.__pontos)):
            self.__texto.posicao[0] += -25
            self.__len_pontuacao += 1

            if len(str(self.__pontos)) >=2:
                self.__fundo.update_width(25)

    def zerar(self):
        self.__velocidade_controller.zerar()
        self.pontos = 0
        self.__len_pontuacao = 1
        self.__texto.posicao = [370, 10]
        self.__fundo.param = [360, 10, 35, 30]

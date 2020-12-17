from singleton import Singleton


class VelocidadeController(metaclass=Singleton):
    def __init__(self):
        self.__vel_inicial = 10
        self.__vel_atual = self.__vel_inicial
        self.__vel_max = 25

        self.__timer = 0
        self.__timer_max = 30

    @property
    def vel_atual(self):
        return self.__vel_atual

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    def zerar(self):
        self.__vel_atual = self.__vel_inicial
        self.__timer = 0

    def update(self):
        if self.__vel_atual <= self.__vel_max:
            self.__timer += 1
            if self.__timer >= self.__timer_max:
                self.__vel_atual += 0.01 * self.__vel_inicial
                self.__timer = 0

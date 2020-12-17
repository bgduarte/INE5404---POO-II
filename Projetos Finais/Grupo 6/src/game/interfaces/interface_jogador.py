from abc import ABC, abstractmethod


class IJogador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def pular(self):
        pass

    @abstractmethod
    def usar(self):
        pass

    @abstractmethod
    def mudar_item(self):
        pass

    @property
    @abstractmethod
    def morto(self):
        pass

    @property
    @abstractmethod
    def inventario(self):
        pass

    @property
    @abstractmethod
    def velocidade(self):
        pass

    @property
    @abstractmethod
    def item_equipado(self):
        pass

    @property
    @abstractmethod
    def posicao(self):
        pass

    @morto.setter
    @abstractmethod
    def morto(self, morto):
        pass

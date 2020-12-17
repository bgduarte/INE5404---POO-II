from abc import ABC, abstractmethod


class IInventario(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def itens(self):
        pass

    #@property
    #@abstractmethod
    #def capacidade(self):
       # pass

    @itens.setter
    @abstractmethod
    def itens(self, itens):
        pass

from abc import ABC, abstractmethod


class IBlococenario(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def quebrar(self):
        pass
    
    @property
    @abstractmethod
    def material(self):
        pass
    
    @property
    @abstractmethod
    def dano(self):
        pass

    @property
    @abstractmethod
    def posicao(self):
        pass

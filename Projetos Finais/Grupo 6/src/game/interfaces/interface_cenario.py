from abc import ABC, abstractmethod


class ICenario(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def fundo(self):
        pass
    
    @property
    @abstractmethod
    def mapa(self):
        pass
    
    @property
    @abstractmethod
    def final(self):
        pass


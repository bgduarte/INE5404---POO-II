from abc import ABC, abstractmethod

#HERANÇA:Jogo herdará da classe abstrata IJOGO
class IJogo (ABC):
    @abstractmethod
    def __init__(self):
        pass
    




    @property
    @abstractmethod
    def jogador (self):
        pass

    @property
    @abstractmethod
    def cenario (self):
        pass


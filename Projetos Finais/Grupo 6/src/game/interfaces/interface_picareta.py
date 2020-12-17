from abc import ABC, abstractmethod
from src.game.ferramenta import Ferramenta 

class IPicareta(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def usar(self):
        pass

from abc import ABC,abstractmethod

class IHud(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass
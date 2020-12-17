from abc import ABC, abstractmethod
class ISistema (ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def selecionar_fase(self, numero_fase):
        pass

    @abstractmethod
    def abrir_opcoes(self):
        pass

    @abstractmethod
    def fechar(self):
        pass

    #@property
    #@abstractmethod
    #def estado_jogo(self):
    #    pass

from abc import ABC, abstractmethod


class IMenuPause(ABC):
    @abstractmethod
    def __init__(self, screen):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def continuar(self):
        pass

    @abstractmethod
    def sair_do_jogo(self):
        pass

    @abstractmethod
    def voltar_menu_principal(self):
        pass

from src.game.ferramenta import Ferramenta
from src.game.interfaces.interface_picareta import IPicareta


class Picareta(Ferramenta, IPicareta):
    def __init__(self):
        super().__init__()
        self.__tipo = "3"
        self.__sprite = self.get_sprites(self.__tipo)

    def get_sprites(self, tipo):
        return super().get_sprites(tipo)

    def usar(self):
        print("Picaretada!")

    @property
    def tipo(self):
        return self.__tipo

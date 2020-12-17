from abc import ABC, abstractmethod
from src.game.interfaces.interface_item import IItem


class Item(IItem):
    def __init__(self, material):
        self.__material = material
        self.__quantidade = 1

    @abstractmethod
    def usar(self):
        pass

    @property
    def material(self):
        return self.__material

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

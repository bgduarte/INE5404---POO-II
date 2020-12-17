import json
import os

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class HUDConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/hud.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def quantidade_slots(self):
        return self.__config["quantidade_slots"]

    @property
    def posicao_slot(self):
        return tuple(self.__config["posicao_slot"])

    @property
    def tamanho_slot(self):
        return tuple(self.__config["tamanho_slot"])

    @property
    def espacamento_slots(self):
        return self.__config["espacamento_slots"]

    @property
    def cor_slot(self):
        return tuple(self.__config["cor_slot"])

    @property
    def tamanho_cursor(self):
        return tuple(self.__config["tamanho_cursor"])

    @property
    def cor_cursor(self):
        return tuple(self.__config["cor_cursor"])

    @property
    def espacamento_cursor(self):
        return self.__config["espacamento_cursor"]

    @property
    def fonte_itens(self):
        return self.__config["fonte_itens"]["fonte"]

    @property
    def tamanho_fonte_itens(self):
        return self.__config["fonte_itens"]["tamanho"]

    @property
    def cor_fonte_itens(self):
        return tuple(self.__config["fonte_itens"]["cor"])

    @property
    def fonte_tempo(self):
        return self.__config["fonte_tempo"]["fonte"]

    @property
    def tamanho_fonte_tempo(self):
        return self.__config["fonte_tempo"]["tamanho"]

    @property
    def cor_fonte_tempo(self):
        return tuple(self.__config["fonte_tempo"]["cor"])

    @property
    def posicao_tempo(self):
        return tuple(self.__config["posicao_tempo"])

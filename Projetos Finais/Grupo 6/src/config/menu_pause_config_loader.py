import json
import os
from os.path import abspath, dirname

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class MenuPauseConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(abspath(dirname(__file__)), "jsons", "menu_pause.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho_botoes(self):
        return tuple(self.__config["tamanho_botoes"])

    @property
    def fonte_botoes(self):
        return self.__config["fonte_botoes"]["fonte"]

    @property
    def tamanho_fonte_botoes(self):
        return self.__config["fonte_botoes"]["tamanho"]

    @property
    def cor_fonte_botoes(self):
        return (self.__config["fonte_botoes"]["cor"])

    @property
    def cor_fundo(self):
        return tuple(self.__config["cor_fundo"])

    @property
    def espacamento(self):
        return tuple(self.__config["espacamento"])

    @property
    def fonte_titulo(self):
        return self.__config["fonte_titulo"]["fonte"]

    @property
    def tamanho_fonte_titulo(self):
        return self.__config["fonte_titulo"]["tamanho"]

    @property
    def cor_fonte_titulo(self):
        return self.__config["fonte_titulo"]["cor"]

    @property
    def cor_fundo_titulo(self):
        return tuple(self.__config["cor_fundo_titulo"])

import json
import os

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class MenuConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.dirname(__file__), "jsons", "menus.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def width_janela(self):
        return self.__config["tamanho_janela"]["width"]

    @property
    def height_janela(self):
        return self.__config["tamanho_janela"]["height"]

    @property
    def fonte_titulo(self):
        return self.__config["fonte_titulo"]["fonte"]

    @property
    def tamanho_fonte_titulo(self):
        return self.__config["fonte_titulo"]["tamanho"]

    @property
    def tamanho_titulo(self):
        return tuple(self.__config["tamanho_titulo"])

    @property
    def fonte_botoes(self):
        return self.__config["fonte_botoes"]["fonte"]

    @property
    def tamanho_fonte_botoes(self):
        return self.__config["fonte_botoes"]["tamanho"]

    @property
    def width_botoes(self):
        return self.__config["tamanho_botoes"]["width"]

    @property
    def height_botoes(self):
        return self.__config["tamanho_botoes"]["height"]

    @property
    def stylesheet(self):
        return self.__config["stylesheet"]

    @property
    def width_fases(self):
        return self.__config["tamanho_fases"]["width"]

    @property
    def height_fases(self):
        return self.__config["tamanho_fases"]["height"]

    @property
    def width_leaderboard(self):
        return self.__config["tamanho_leaderboard"]["width"]

    @property
    def height_leaderboard(self):
        return self.__config["tamanho_leaderboard"]["height"]

    @property
    def fonte_leaderboard(self):
        return self.__config["fonte_leaderboard"]["fonte"]

    @property
    def tamanho_fonte_leaderboard(self):
        return self.__config["fonte_leaderboard"]["tamanho"]

    @property
    def width_input_jogador(self):
        return self.__config["tamanho_input_jogador"]["width"]

    @property
    def height_input_jogador(self):
        return self.__config["tamanho_input_jogador"]["height"]

    @property
    def fonte_input_jogador(self):
        return self.__config["fonte_input_jogador"]["fonte"]

    @property
    def tamanho_fonte_input_jogador(self):
        return self.__config["fonte_input_jogador"]["tamanho"]

    @property
    def fonte_botoes_fase(self):
        return self.__config["fonte_botoes_fase"]["fonte"]
    
    @property
    def tamanho_fonte_botoes_fase(self):
        return self.__config["fonte_botoes_fase"]["tamanho"]

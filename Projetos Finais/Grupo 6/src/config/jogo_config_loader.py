import os
import json

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class JogoConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/jogo.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    def obter_mapa(self, n):
        return self.__config["mapas"][str(n)]

    def obter_fundo(self, n):
        return os.path.join(self.diretorio_assets, "fundos", f"fundo{n}.jpg")

    def obter_final(self, n):
        return self.__config["mapas"][str(n)]["final"]

    def obter_posicao_inicial(self, n):
        return self.__config["mapas"][str(n)]["posicao_inicial"]

    @property
    def width_janela(self):
        return self.__config["tamanho_janela"]["width"]

    @property
    def height_janela(self):
        return self.__config["tamanho_janela"]["height"]

    @property
    def diretorio_sprites(self):
        return os.path.join(os.getenv('PYTHONPATH'), "assets", "sprites")

    @property
    def tamanho_fonte(self):
        return self.__config["tamanho_fonte"]

    @property
    def cor_fonte(self):
        return self.__config["cor_fonte"]

    @property
    def fonte(self):
        return self.__config["fonte"]
    
    @property
    def posicao_texto(self):
        return self.__config["posicao_texto"]

    @property
    def icone(self):
        return os.path.join(self.diretorio_assets, "icon", "icon.png")

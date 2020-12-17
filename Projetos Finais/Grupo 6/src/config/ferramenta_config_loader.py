import os
import json
import pygame

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class FerramentaConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        super().__init__()
        self.__tamanho = [30,30]
        self.load()

    def load(self):
        pass

    def recortar_sprites(self, ferramenta):
        sprite = pygame.image.load(f"{self.diretorio_sprites}/{ferramenta}.png")
        return sprite

    @property
    def diretorio_sprites(self):
        return os.path.join(self.diretorio_assets, "sprites/ferramentas")

    @property
    def tamanho(self):
        return self.__tamanho

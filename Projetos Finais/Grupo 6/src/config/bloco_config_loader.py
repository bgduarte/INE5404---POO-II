import json
import os
import pygame

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class BlocoConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/blocos.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho_original(self):
        return tuple(self.__config["tamanho"])

    @property
    def tamanho(self):
        return self.__config["tamanho"][0]*2, self.__config["tamanho"][1]*2

    @property
    def diretorio_sprites(self):
        return os.path.join(self.diretorio_assets, "sprites", "blocos")

    def obter_sprites(self, material):
        print(material)
        sprite_base = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, str(material), "block.png")), tuple(self.tamanho))
        sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, str(material), "blockdmg1.png")), tuple(self.tamanho))
        sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, str(material), "blockdmg2.png")), tuple(self.tamanho))
        sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, str(material), "blockdmg3.png")), tuple(self.tamanho))

        return {"base":sprite_base,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3}

    def obter_sprite_original(self, material):
        return pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/block.png"))

    def obter_dados(self, material, dado):
        if dado =="dano":
            return self.__config["dano"][material]
        elif dado=="vida":
            return self.__config["vida"][material]
         

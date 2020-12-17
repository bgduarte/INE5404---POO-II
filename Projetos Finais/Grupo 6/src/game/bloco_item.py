from src.config.bloco_config_loader import BlocoConfigLoader
from src.game.item import Item
import pygame

class BlocoItem(Item):
    def __init__(self, material, posicao):
        super().__init__(material)
        self.__config = BlocoConfigLoader()
        self.__material = material
        self.__sprite = self.__config.obter_sprite_original(self.__material)
        self.__posicao = posicao
        self.__hitbox = pygame.Rect(self.__posicao[0], self.__posicao[1], 5, 5)
        

    def atualizar(self):
        pass

    def usar(self):
        pass

    @property
    def sprite(self):
        return self.__sprite

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        return self.__posicao

    @property
    def tamanho(self):
        return self.__config.tamanho_original

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material


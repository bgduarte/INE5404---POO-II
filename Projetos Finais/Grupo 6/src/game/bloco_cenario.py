import os
import pygame

from src.game.interfaces.interface_bloco_cenario import IBlococenario
from src.config.bloco_config_loader import BlocoConfigLoader


class BlocoCenario(IBlococenario):
    def __init__(self, material:int,posicao:list):
        self.__config = BlocoConfigLoader()
        self.__material = material
        self.__dano = self.__config.obter_dados(material,"dano")
        self.__vida = self.__config.obter_dados(material,"vida")
        self.__posicao = posicao
        self.__sprites = self.__config.obter_sprites(material)
        self.__sprite = self.__sprites["base"]
        #self.__sprite = pygame.transform.scale(self.__sprite, (44, 32))
        self.__tamanho_hitbox = (44, 32)
        self.__hitbox = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho_hitbox[0], self.__tamanho_hitbox[1])
        
    
    def atualizar(self):
        if self.__vida < 4:
           #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-3.png")), (44,32))
           self.__sprite=self.__sprites["dmg3"]
        elif self.__vida < 8:
            #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-3.png")), (44,32))
            #screen.blit(self.__sprites["dmg2"], tuple(self.__posicao))
            self.__sprite=self.__sprites["dmg2"]
        elif self.__vida < 12:
            #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-2.png")), (44,32))
            #screen.blit(self.__sprites["dmg1"], tuple(self.__posicao))
            self.__sprite=self.__sprites["dmg1"]
        elif self.__vida < 16:
            #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-1.png")), (44,32))
            #screen.blit(self.__sprites["base"], tuple(self.__posicao))
            self.__sprite=self.__sprites["base"]
            ##print ("base")
        ##elif self.__vida < 12:
            #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-2.png")), (44,32))
            #screen.blit(self.__sprites["dmg1"], tuple(self.__posicao))
            ##self.__sprite=self.__sprites["dmg1"]
          ##  print ("dmg1")
        ##elif self.__vida < 8:
            #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-3.png")), (44,32))
            #screen.blit(self.__sprites["dmg2"], tuple(self.__posicao))
            ##self.__sprite=self.__sprites["dmg2"]
        ##elif self.__vida < 4:
           #self.__sprite = pygame.transform.scale(pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box-dmg-3.png")), (44,32))
           ##self.__sprite=self.__sprites["dmg3"]
        #screen.blit(self.__sprite, tuple(self.__posicao))    
    def quebrar(self):
        pass

    @property
    def material(self):
        return self.__material

    @property
    def dano(self):
        return self.__dano

    @property
    def posicao(self):
        return self.__posicao

    @property
    def sprite(self):
        return self.__sprite

    @property
    def tamanho_hitbox(self):
        return self.__tamanho_hitbox

    @property
    def hitbox(self):
        return self.__hitbox

    @property
    def vida(self):
        return self.__vida   

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @material.setter
    def material(self, material):
        self.__material = material

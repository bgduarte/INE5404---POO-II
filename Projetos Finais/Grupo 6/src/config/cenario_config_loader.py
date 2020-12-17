import os
import json
import pygame

from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class CenarioConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/mapas.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    def obter_mapa(self,mapa):
        mapablocos=[]
        print (len(self.__config[mapa]))
        for y in range (0,len(self.__config[mapa])):
            mapablocos.append(list(self.__config[mapa][y]))
        return mapablocos

    def obter_fim(self,mapa):
        return self.__config["finais"][mapa]

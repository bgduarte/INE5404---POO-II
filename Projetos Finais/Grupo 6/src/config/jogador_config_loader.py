import os
import json
import pygame
from pygame.transform import scale, flip


from src.config.config_loader import ConfigLoader
from src.config.singleton import Singleton


class JogadorConfigLoader(ConfigLoader, Singleton):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/jogador.json")
        self.load()
        self.__tamanho_original = [37*2, 28*2]

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho(self):
        return self.__tamanho_original[0] * 2, self.__tamanho_original[1] * 2

    @property
    def diretorio_sprites(self):
        #codigo do path do bings - meu pythonpath tem 2 variáveis
        #return "C:/Users/Arthur/Projects/projeto-final-pooII/assets/sprites/"
        return os.path.join(self.diretorio_assets, "sprites/")



    def recortar_sprites(self):


        
        #sprites martelo ---------------------------------------
        sprite_idle = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-martelo/idle.png"))
        sprite_run_right = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-martelo/runRight.png"))
        sprite_attack = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-martelo/attack.png"))
        sprite_pulo = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-martelo/jump.png")), self.tamanho)
        sprite_pulo_invertido = flip(sprite_pulo, 1, 0)
        sprite_queda = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-martelo/fall.png")), self.tamanho)
        sprite_queda_invertido = flip(sprite_queda, 1, 0)

        lista_martelo = [sprite_idle, sprite_run_right, sprite_attack, sprite_pulo, sprite_pulo_invertido, sprite_queda]

        #sprites pa ---------------------------------------
        sprite_idle = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-pa/idle.png"))
        sprite_run_right = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-pa/runRight.png"))
        sprite_attack = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-pa/attack.png"))
        sprite_pulo = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-pa/jump.png")), self.tamanho)
        sprite_pulo_invertido = flip(sprite_pulo, 1, 0)
        sprite_queda = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-pa/fall.png")), self.tamanho)
        sprite_queda_invertido = flip(sprite_queda, 1, 0)

        lista_pa = [sprite_idle, sprite_run_right, sprite_attack, sprite_pulo, sprite_pulo_invertido, sprite_queda]

        #sprites picareta ---------------------------------------
        sprite_idle = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-picareta/idle.png"))
        sprite_run_right = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-picareta/runRight.png"))
        sprite_attack = pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-picareta/attack.png"))
        sprite_pulo = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-picareta/jump.png")), self.tamanho)
        sprite_pulo_invertido = flip(sprite_pulo, 1, 0)
        sprite_queda = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "sprites-picareta/fall.png")), self.tamanho)
        sprite_queda_invertido = flip(sprite_queda, 1, 0)

        lista_picareta = [sprite_idle, sprite_run_right, sprite_attack, sprite_pulo, sprite_pulo_invertido, sprite_queda]

        #outros sprites que possuem uma lista

        lista_sprites_temp = [lista_martelo, lista_pa, lista_picareta, lista_martelo,lista_martelo,lista_martelo]
        lista_sprites = []

        #For que itera sobre todas os sprites das listas
        for m in range(len(lista_sprites_temp)):
            lista_atual_sprites = lista_sprites_temp[m]
            
            sprite_idle_atual = lista_atual_sprites[0]
            sprite_run_right_atual = lista_atual_sprites[1]
            sprite_attack_atual = lista_atual_sprites[2]
            sprite_pulo_atual = lista_atual_sprites[3]
            sprite_pulo_invertido_atual = lista_atual_sprites[4]
            sprite_queda_atual = lista_atual_sprites[5]

            sprites_idle = []
            sprites_idle_invertido = []
            sprites_run_left = []
            sprites_run_right = []
            sprites_attack = []
            sprites_attack_invertido = []

            for i in range(11):
                sprites_idle.append(scale(sprite_idle_atual.subsurface(pygame.Rect(78 * i, 0, self.__tamanho_original[0], self.__tamanho_original[1])), self.tamanho))
                sprites_idle_invertido.append(flip(sprites_idle[i], 1, 0))

            for j in range(8):
                sprites_run_right.append(scale(sprite_run_right_atual.subsurface(pygame.Rect(78 * j, 0, self.__tamanho_original[0], self.__tamanho_original[1])), self.tamanho))
                sprites_run_left.append(flip(sprites_run_right[j], 1, 0))    


            for k in range(3):
                sprites_attack.append(scale(sprite_attack_atual.subsurface(pygame.Rect(78*k, 0, self.__tamanho_original[0], self.__tamanho_original[1])),self.tamanho))

            sprites_attack_invertido.append(flip(sprites_attack[0],1,0))
            sprites_attack_invertido.append(flip(sprites_attack[1],1,0))
            sprites_attack_invertido.append(flip(sprites_attack[2],1,0))

            
            spriteDic = {"left": sprites_run_left, "right": sprites_run_right, "idle": sprites_idle, "idleM": sprites_idle_invertido,
                "attack": sprites_attack, "attackM": sprites_attack_invertido, "jump": sprite_pulo_atual, "jumpM": sprite_pulo_invertido_atual,
                "fall": sprite_queda_atual, "fallM": sprite_queda_invertido}

            lista_sprites.append(spriteDic)

        return lista_sprites

    @property
    def massa(self):
        return self.__config["massa"]

    @property
    def tamanho_pulo(self):
        return self.__config["massa"]

    @property
    def velocidade(self):
        return self.__config["velocidade"]

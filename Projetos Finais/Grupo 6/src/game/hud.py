import pygame
from pygame.locals import *
from pygame.transform import scale

from src.config.hud_config_loader import HUDConfigLoader
from src.game.interfaces.interface_hud import IHud
from src.game.jogador import Jogador
from src.game.bloco_item import BlocoItem


class HUD(IHud):
    def __init__(self):
        self.__config = HUDConfigLoader()
        #adcionar imagens de slot de inventario
        self.__slots = [pygame.Surface(self.__config.tamanho_slot) for i in range(self.__config.quantidade_slots)]
        self.__cursor = pygame.Surface(self.__config.tamanho_cursor)
        self.__cursor.fill(self.__config.cor_cursor)

    def atualizar(self, jogador, screen, tempo):
        tempo = pygame.font.Font(pygame.font.match_font(self.__config.fonte_tempo), self.__config.tamanho_fonte_tempo).render(f"Tempo: {tempo}s", True, self.__config.cor_fonte_tempo)
        screen.blit(tempo, self.__config.posicao_tempo)
        screen.blit(self.__cursor, (self.__config.posicao_slot[0] + jogador.item_equipado*(self.__config.tamanho_slot[0] + self.__config.espacamento_slots),
                                    self.__config.posicao_slot[1] + self.__config.tamanho_slot[1] + self.__config.espacamento_cursor))
        for i in range (len(self.__slots)):

            self.__slots[i].fill(self.__config.cor_slot)
            screen.blit(self.__slots[i], (self.__config.posicao_slot[0] + self.__slots.index(self.__slots[i])*(self.__config.tamanho_slot[0] + self.__config.espacamento_slots), self.__config.posicao_slot[1]))
            item = jogador.inventario.itens[i]
            try:
                #TODO eliminar hard coded references 5 e 8
                screen.blit(scale(item.sprite, self.__config.tamanho_slot), (self.__config.posicao_slot[0] + i*(self.__config.tamanho_slot[0] + self.__config.espacamento_slots), self.__config.posicao_slot[1]))
            except AttributeError as e:
                print(e)

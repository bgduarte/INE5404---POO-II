import pygame

from src.game.bloco_item import BlocoItem
from src.game.bloco_cenario import BlocoCenario
from src.game.interfaces.interface_cenario import ICenario
from src.config.jogo_config_loader import JogoConfigLoader

class Cenario(ICenario):
    def __init__(self, mapa):
        self.__config = JogoConfigLoader()
        self.__fundo = self.__config.obter_fundo(mapa)
        self.__mapa = []
        blocos = self.__config.obter_mapa(mapa)["blocos"]
        for y in range(len(blocos)):
            for x in range((len(blocos[y]))):
                try:
                    self.__mapa.append(BlocoCenario(int(blocos[y][x]), [x*33, y*36]))
                #Uso de exceções:Se o material for 0 ele não vai encontrar sprite, consequentemente não via criar o bloco
                except FileNotFoundError as e:
                    print (e)
                    pass

        self.__final = self.__config.obter_final(mapa)
        #itens no chão
        self.__itens = []
        self.__hitbox_blocos = [bloco.hitbox for bloco in self.__mapa]


    def quebrar(self, bloco,ferramenta):
        try:
            if bloco.vida <= bloco.dano[ferramenta]:
                self.__mapa.remove(bloco)
                self.__itens.append(BlocoItem(bloco.material, [bloco.hitbox.x + bloco.tamanho_hitbox[0]//2, bloco.hitbox.y + bloco.tamanho_hitbox[1]]))
                return True
            else:
                bloco.vida -= bloco.dano[ferramenta]
                bloco.atualizar()
                return False
        except Exception:
            pass

    def atualizar(self, screen):
        for bloco in self.__mapa:
            screen.blit(bloco.sprite, (bloco.hitbox.x, bloco.hitbox.y))
            #pygame.draw.rect(screen, (255, 0, 0), bloco.hitbox, 2)
        
        for item in self.__itens:
            screen.blit(item.sprite, (item.hitbox.x, item.hitbox.y))

    def remover_item(self, item):
        self.__itens.remove(item)


    def adicionar_bloco_cenario(self, item: BlocoItem, pos: list, last_side: int):
        #Criar bloco
        if last_side == 1:
            bloco = BlocoCenario(item.material, [pos[0] + 60, pos[1] + 24])
            
        else:
            bloco = BlocoCenario(item.material, [pos[0] - 60, pos[1] + 24])

        pos_cen = 0
        
        while pos_cen < len(self.__mapa):
            bloco_cen = self.__mapa[pos_cen]

            if bloco.hitbox.colliderect(bloco_cen.hitbox):
                bloco.hitbox.y -= 36
                pos_cen = -1

            pos_cen += 1


        #Adicionar o bloco ao cenário
        self.__mapa.append(bloco)

    def remover_bloco_mapa(self, bloco):
        self.__mapa.remove(bloco)

    @property
    def fundo(self):
        return self.__fundo

    @property
    def mapa(self):
        return self.__mapa

    @property
    def final(self):
        return self.__final

    @property
    def hitbox_blocos(self):
        return self.__hitbox_blocos

    @property
    def itens(self):
        return self.__itens

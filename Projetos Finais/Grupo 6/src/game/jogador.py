from src.game.bloco_item import BlocoItem
from PyQt5.QtCore import right
import pygame
from pygame.locals import *

from src.config.jogador_config_loader import JogadorConfigLoader
from src.exceptions.tipo_nao_compativel_exception import TipoNaoCompativelException
from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.item import Item
from src.game.ferramenta import Ferramenta



class Jogador(IJogador):
    def __init__(self, nome: str, posicao_inicial: list):
        self.__config = JogadorConfigLoader()
        self.__nome = nome
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = self.__config.velocidade

        #teste
        self.__lista_velocidade = [0, 0]
        self.__momentum = [0,0]

        self.__item_equipado = 0
        self.__posicao = posicao_inicial
        self.__massa = self.__config.massa
        self.__tamanho_pulo = self.__config.tamanho_pulo

        #dicionário para os sprites
        self.__sprites = self.__config.recortar_sprites()

        #bools para determinar qual animação o personagem está realizando
        self.__left = False
        self.__right = False
        #bool para saber a ultima direção que o personagem estava virado - 0 -> esquerda, 1 -> direita
        self.__last_side = 1
        self.__is_jump = False
        self.__is_attack = False
        self.__is_use = False
        self.__is_idle = True
        self.__is_fall = False
        self.__pode_mover_direita = True
        self.__pode_mover_esquerda = True

        #test
        self.__teste_velocidade = [0,0]
        self.__teste_movimento = [0,0]

        #contadores para o pulo e a animação de correr
        self.__walk_count = 0
        self.__jump_count = self.__tamanho_pulo
        self.__idle_count = 0
        self.__attack_count = 0
        self.__tamanho_hitbox = (self.__config.tamanho[0]/2, self.__config.tamanho[1]/2)
        self.__hitbox = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho_hitbox[0] - 25, self.__tamanho_hitbox[1])

    def atualizar(self, tecla, screen):
        self.mover(tecla)
        if self.__walk_count + 1 >= 24:
            self.__walk_count = 0

        if self.__idle_count + 1 >= 33:
            self.__idle_count = 0

        if self.__is_attack:
            if self.__last_side == 1:
                if self.__left:
                    screen.blit(self.__sprites["attackM"][self.__attack_count //4], tuple(self.__posicao))
                    self.__attack_count += 1
                    self.__last_side = 0
                else:    
                    screen.blit(self.__sprites["attack"][self.__attack_count //4], tuple(self.__posicao))
                    self.__attack_count += 1

            else:
                if self.__right:
                    screen.blit(self.__sprites["attack"][self.__attack_count //4], tuple(self.__posicao))
                    self.__last_side = 1
                    self.__attack_count += 1
                else:
                    screen.blit(self.__sprites["attackM"][self.__attack_count //4], tuple(self.__posicao))
                    self.__attack_count += 1

        elif not self.__is_fall and self.__is_jump:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
            else:
                if self.right:
                    self.__last_side = 1
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))

        elif self.__is_fall:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["fall"], tuple(self.__posicao))
            else:
                if self.right:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["fallM"], tuple(self.__posicao))

        elif self.__left:
            screen.blit(self.__sprites["left"][self.__walk_count // 3], tuple(self.__posicao))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 0

        elif self.__right:
            screen.blit(self.__sprites["right"][self.__walk_count // 3], tuple(self.__posicao))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 1

        elif self.__is_idle == True and self.__is_attack == False:
            #idle pra esquerda e idle pra direita
            if self.__last_side == 1:
                #direita
                screen.blit(self.__sprites["idle"][self.__idle_count // 3], tuple(self.__posicao))
                self.__idle_count += 1

            else:
                #esquerda
                screen.blit(self.__sprites["idleM"][self.__idle_count // 3], tuple(self.__posicao))
                self.__idle_count += 1

        if self.__right or self.__last_side == 1:
            self.__hitbox.x = self.__posicao[0] + 32
            self.__hitbox.y = self.__posicao[1] + 36
        else:
            self.__hitbox.x = self.__posicao[0] + 50
            self.__hitbox.y = self.__posicao[1] + 36
        

        self.mudar_item(tecla)
        #pygame.draw.rect(screen, (255, 0, 0), self.__hitbox, 2)

    def atualizar_teste(self, screen):
        #O Segredo é sempre ajustar o sprite e NÃO o hitbox

        #posicao ajustada dos nosso sprites
        pos = self.__hitbox.x - 35

        #Em alguns blits será possível ver que subtraimos mais 30, isso acontece pelo sprite virado ter que ser ajustado de novo

        if self.__walk_count + 1 >= 24:
            self.__walk_count = 0

        if self.__idle_count + 1 >= 33:
            self.__idle_count = 0

        if self.__is_attack:
            if self.__last_side == 1:
                if self.__left:
                    screen.blit(self.__sprites[self.__item_equipado]["attackM"][self.__attack_count //4], (pos - 30, self.__hitbox.y - 30))
                    self.__attack_count += 1
                    self.__last_side = 0
                else:    
                    screen.blit(self.__sprites[self.__item_equipado]["attack"][self.__attack_count //4], (pos, self.__hitbox.y - 30))
                    self.__attack_count += 1

            else:
                if self.__right:
                    screen.blit(self.__sprites[self.__item_equipado]["attack"][self.__attack_count //4], (pos, self.__hitbox.y - 30))
                    self.__last_side = 1
                    self.__attack_count += 1
                else:
                    screen.blit(self.__sprites[self.__item_equipado]["attackM"][self.__attack_count //4], (pos - 30, self.__hitbox.y - 30))
                    self.__attack_count += 1

        elif not self.__is_fall and self.__is_jump:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites[self.__item_equipado]["jumpM"], (pos - 30, self.__hitbox.y - 30))
                else:
                    screen.blit(self.__sprites[self.__item_equipado]["jump"], (pos, self.__hitbox.y - 30))
            else:
                if self.right:
                    self.__last_side = 1
                    screen.blit(self.__sprites[self.__item_equipado]["jump"], (pos, self.__hitbox.y - 30))
                else:
                    screen.blit(self.__sprites[self.__item_equipado]["jumpM"], (pos - 30, self.__hitbox.y - 30))

        elif self.__is_fall:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites[self.__item_equipado]["jumpM"], (pos - 30, self.__hitbox.y - 30))
                else:
                    screen.blit(self.__sprites[self.__item_equipado]["fall"],(pos, self.__hitbox.y - 30))
            else:
                if self.right:
                    self.__last_side = 0
                    screen.blit(self.__sprites[self.__item_equipado]["jump"], (pos, self.__hitbox.y - 30))
                else:
                    screen.blit(self.__sprites[self.__item_equipado]["fallM"], (pos - 30, self.__hitbox.y - 30))

        elif self.__left:
            screen.blit(self.__sprites[self.__item_equipado]["left"][self.__walk_count // 3], (pos - 30, self.__hitbox.y - 30))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 0

        elif self.__right:
            screen.blit(self.__sprites[self.__item_equipado]["right"][self.__walk_count // 3], (pos, self.__hitbox.y - 30))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 1

        elif self.__is_idle == True and self.__is_attack == False:
            #idle pra esquerda e idle pra direita
            if self.__last_side == 1:
                #direita
                screen.blit(self.__sprites[self.__item_equipado]["idle"][self.__idle_count // 3], (pos, self.__hitbox.y - 30))
                self.__idle_count += 1

            else:
                #esquerda
                screen.blit(self.__sprites[self.__item_equipado]["idleM"][self.__idle_count // 3], (pos - 30, self.__hitbox.y - 30))
                self.__idle_count += 1

        """ if self.__right or self.__last_side == 1:
            self.__hitbox.x += 32
            self.__hitbox.y += 36
        else:
            self.__hitbox.x += 50
            self.__hitbox.y += 36 """
        

        #self.mudar_item(tecla)
        #pygame.draw.rect(screen, (255, 0, 0), self.__hitbox, 2)


    def mover(self, tecla):
        pass

    def pular(self):
        pass


    def usar(self, key):
        if key == pygame.K_e:
            #Como ele tem a habilidade de colocar blocos, n necessariamente is_attack se torna verdade

            #Utilidade da herança de ferramenta: Será conferido a instância de uma ferramenta como item equipado
            #Assim,poderá ser definido se o jogador está em estado de ataque
            if isinstance(self.__inventario.itens[self.__item_equipado], Ferramenta):
                self.__is_attack = True
        
        if self.__attack_count >= 11:
            self.__attack_count = 0
            self.__is_attack = False
            self.__is_idle = True

        elif self.__attack_count == 0:
            try:
                self.__inventario.itens[self.__item_equipado].usar()
                print("usou!")
            except AttributeError:
                print("Sem Item")
                self.__is_attack = False
                self.__attack_count = 0
                #Uso de exceções,usado para otimizar o processo de uso dos itens.
            else:
                self.__attack_count += 1


    def mudar_item(self, tecla):
        if tecla[pygame.K_1]:
            self.__item_equipado = 0
        elif tecla[pygame.K_2]:
            self.__item_equipado = 1
        elif tecla[pygame.K_3]:
            self.__item_equipado = 2
        elif tecla[pygame.K_4]:
            self.__item_equipado = 3
        elif tecla[pygame.K_5]:
            self.__item_equipado = 4
        elif tecla[pygame.K_6]:
            self.__item_equipado = 5


    def adicionar_item(self, item: Item):
        if isinstance(item, Item):
            try:
                i = self.__inventario.itens.index(None)
                add = False

                if isinstance(item, BlocoItem):
                    for item_inv in self.__inventario.itens:
                        if isinstance(item_inv, BlocoItem) and item.material == item_inv.material:
                            item_inv.quantidade += 1
                            add = True
                            
                if not add:
                    self.__inventario.itens[i] = item


            except ValueError:
                print("Inventário cheio")
        else:
            raise TipoNaoCompativelException

    def remover_item(self, item: Item):
        if item.quantidade > 1:
            item.quantidade -= 1
        else:
            try:
                self.__inventario.itens.remove(item)
            except Exception as e:
                print(e)
                



    @property
    def morto(self):
        return self.__morto

    @morto.setter
    def morto(self, morto):
        self.__morto = morto

    @property
    def inventario(self):
        return self.__inventario

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def item_equipado(self):
        return self.__item_equipado

    @property
    def posicao(self):
        return self.__posicao

    @property
    def sprites(self):
        return self.__sprites

    @property
    def walk_count(self):
        return self.__walk_count

    @walk_count.setter
    def walk_count(self, walk_count):
        self.__walk_count = walk_count

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def idle_count(self):
        return self.__idle_count

    @idle_count.setter
    def idle_count(self, idle_count):
        self.__idle_count = idle_count

    @property
    def last_side(self):
        return self.__last_side

    @last_side.setter
    def last_side(self, last_side):
        self.__last_side = last_side

    @property
    def is_attack(self):
        return self.__is_attack

    @is_attack.setter
    def is_attack(self, is_attack):
        self.__is_attack = is_attack

    @property
    def attack_count(self):
        return self.__attack_count

    @attack_count.setter
    def attack_count(self, attack_count):
        self.__attack_count = attack_count

    @property
    def is_idle(self):
        return self.__is_idle

    @is_idle.setter
    def is_idle(self, is_idle):
        self.__is_idle = is_idle

    @property
    def is_fall(self):
        return self.__is_fall

    @is_fall.setter
    def is_fall(self, is_fall):
        self.__is_fall = is_fall

    @property
    def is_jump(self):
        return self.__is_jump

    @is_jump.setter
    def is_jump(self, is_jump):
        self.__is_jump = is_jump

    @property
    def pode_mover_direita(self):
        return self.__pode_mover_direita

    @pode_mover_direita.setter
    def pode_mover_direita(self, pode_mover_direita):
        self.__pode_mover_direita = pode_mover_direita

    @property
    def pode_mover_esquerda(self):
        return self.__pode_mover_esquerda

    @pode_mover_esquerda.setter
    def pode_mover_esquerda(self, pode_mover_esquerda):
        self.__pode_mover_esquerda = pode_mover_esquerda

    @property
    def tamanho_hitbox(self):
        return self.__tamanho_hitbox

    @property
    def hitbox(self):
        return self.__hitbox

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property 
    def lista_velocidade(self):
        return self.__lista_velocidade

    @lista_velocidade.setter
    def lista_velocidade(self, lista_velocidade):
        self.__lista_velocidade = lista_velocidade

    @property
    def momentum(self):
        return self.__momentum

    @momentum.setter
    def momentum(self, momentum):
        self.__momentum = momentum

    @property
    def teste_velocidade(self):
        return self.__teste_velocidade

    @teste_velocidade.setter
    def teste_velocidade(self, velocidade_y):
        self.__teste_velocidade = velocidade_y

    @property
    def teste_movimento(self):
        return self.__teste_movimento

    @teste_movimento.setter
    def teste_movimento(self, teste_movimento):
        self.__teste_movimento = teste_movimento

    @property
    def is_use(self):
        return self.__is_use

    @is_use.setter
    def is_use(self, is_use):
        self.__is_use = is_use

    @property
    def nome(self):
        return self.__nome

from objetos_controller import ObjetosController
from pontuacao_controller import PontuacaoController
from efeito import Efeito
from vacina import Vacina
from mascara import Mascara
from alcool_gel import AlcoolGel
import pygame
import random


class EfeitoController(ObjetosController):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.__pontuacao_controller = PontuacaoController()
        self.__efeitos = ["vacina", "mascara", "alcool_gel"]
        self.__posicoes_efeitos = [[[35, -100], [145, -100], [260, -100]], [[35, -400], [145, -400], [260, -400]]]

    def cria_objeto(self):
        chance = random.randint(1,50)
        if chance == 1:
            escolhe_posicoes = random.randint(0, 1)
            pista = random.randint(0, 2)
            if len(self.pistas[pista]) == 0:
                posicao_efeito = self.__posicoes_efeitos[escolhe_posicoes][pista]
                escolhe_efeito = random.choice(self.__efeitos)
                efeito = None
                if escolhe_efeito == "vacina":
                    efeito = Vacina(posicao_efeito, self.jogador)
                elif escolhe_efeito == "mascara":
                    efeito = Mascara(posicao_efeito, self.jogador)
                elif escolhe_efeito == "alcool_gel":
                    efeito = AlcoolGel(posicao_efeito)
                if efeito != None:
                    self.pistas[pista].add(efeito)

    def timer_update(self):
        self.timer += 1
        if self.timer > self.timer_max:
            self.cria_objeto()
            self.timer = 0
            if self.timer_max > 15:
                if self.velocidade_controller.vel_atual >= self.limite_vel:
                    self.timer_max -= 1
                    self.limite_vel += 1

    def draw(self):
        for pista in self.pistas:
            for efeito in pista:
                efeito.blitme()

    def update(self):
        for pista in self.pistas:
            for efeito in pista:
                efeito.update()
        self.check_colisao()

    def check_colisao(self):  
        for i in range(3):
            bateu = pygame.sprite.spritecollideany(self.jogador, self.pistas[i])
            #Colisao com efeitos
            if isinstance(bateu, Efeito):
                bateu.efeito()
                bateu.kill()
                del bateu
                if len(self.som_controller.sounds_efeitos) >= 1:
                    self.som_controller.play_sound_efeitos(0)

    def parar_efeitos(self):
        #Mascara
        self.jogador.invencivel = False
        self.jogador.timer_invencivel = 0
        #Alcool Gel
        self.__pontuacao_controller.multiplicador = 1
        self.__pontuacao_controller.multiplicador_ativo = False
        self.__pontuacao_controller.timer_multiplicador = 0

    def zerar(self):
        super().zerar()
        self.parar_efeitos()

from objetos_controller import ObjetosController
from obstaculo import Obstaculo
import pygame
import random


class ObstaculoController(ObjetosController):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.__obstaculos_tela = ["Materials/virus.png", "Materials/EAD.png"]
        self.__posicoes_obstaculos = [[35, -250], [145, -250], [260, -250]]
        
    def cria_objeto(self, qtd):
        for _ in range(qtd):
            pista = random.randint(0, 2)
            if len(self.pistas[pista]) == 0:
                posicao = self.__posicoes_obstaculos[pista]
                image = random.choice(self.__obstaculos_tela)
                obstaculo = Obstaculo(posicao,
                            [pygame.image.load(image).convert_alpha(self.tela.display)])
                self.pistas[pista].add(obstaculo)

    def timer_update(self):
        self.timer += 1
        if self.timer > self.timer_max:
            self.cria_objeto(random.randint(1, 2))
            self.timer = 0
            if self.timer_max > 15:
                if self.velocidade_controller.vel_atual >= self.limite_vel:
                    self.timer_max -= 1
                    self.limite_vel += 1

    def draw(self):
        for pista in self.pistas:
            for obstaculo in pista:
                obstaculo.blitme()

    def update(self):
        for pista in self.pistas:
            for obstaculo in pista:
                obstaculo.update()
        self.check_colisao()

    def check_colisao(self):
        for i in range(3):
            bateu = pygame.sprite.spritecollideany(self.jogador, self.pistas[i])
            #Colisao com obstaculos
            if isinstance(bateu, Obstaculo):
                bateu.kill()
                del bateu
                if not self.jogador.invencivel:
                    self.jogador.perde_vida()
                    if len(self.som_controller.sounds_obstaculos) > 0:
                        self.som_controller.play_sound_obstaculos(random.randint(0, len(self.som_controller.sounds_obstaculos) - 1))
                else:
                    if len(self.som_controller.sounds_efeitos) >= 2:
                        self.som_controller.play_sound_efeitos(1)

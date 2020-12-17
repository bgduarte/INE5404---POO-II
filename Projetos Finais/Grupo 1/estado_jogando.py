from estado import Estado
from events_jogando import EventsJogando
from fundo import Fundo
from botao_imagem import BotaoImagem
import pygame


class EstadoJogando(Estado):
    def __init__(self, jogador, obstaculo_controller, efeito_controller):
        super().__init__(jogador, obstaculo_controller, efeito_controller)
        self.__events_jogando = EventsJogando(self.jogador)
        self.__borda = pygame.image.load("Materials/borda.png").convert_alpha(self.tela.display)
        self.__vida = pygame.image.load("Materials/coracao.png").convert_alpha(self.tela.display)
        self.__mascara = pygame.image.load("Materials/mascara menor.png").convert_alpha(self.tela.display)
        self.__alcool_gel = pygame.image.load("Materials/alcool gel menor.png").convert_alpha(self.tela.display)
        
        self.__imagem_pausa = pygame.image.load("Materials/pausa.png").convert_alpha(self.tela.display)
        self.__fundo_pausa = Fundo([10, 10, 50, 50], self.WHITE)
        self.__botao_pausa = BotaoImagem(self.__imagem_pausa, [15, 15], self.__fundo_pausa, self.GREEN, self.DARK_GREEN, self.__events_jogando)

    def start(self):
        # Updates
        self.__events_jogando.check_events()
        self.fases_controller.update()
        self.fases_controller.fase_atual.update()
        morreu = self.jogador.update()
        self.pontuacao.update()
        self.obstaculo_controller.update()
        self.efeito_controller.update()
        self.obstaculo_controller.timer_update()
        self.efeito_controller.timer_update()
        self.velocidade_controller.update()

        pausa_botao = self.__botao_pausa.update()

        # Draws
        self.fases_controller.fase_atual.blitme()
        self.jogador.blitme()
        self.obstaculo_controller.draw()
        self.efeito_controller.draw()
        self.pontuacao.fundo.blitme()
        self.pontuacao.draw()
        self.__botao_pausa.draw()

        # Draw no numero de vidas
        for i in range(self.jogador.vida_atual):
            self.tela.display.blit(self.__vida, (350, 100 + 40*i))
        
        # Draw nos efeitos
        if self.jogador.invencivel:
            self.tela.display.blit(self.__mascara, (350, 230))

        if self.pontuacao.multiplicador_ativo:
            self.tela.display.blit(self.__alcool_gel, (350, 280))


        # Desenha borda na tela
        self.tela.display.blit(self.__borda, (0, 0))

        if self.__events_jogando.pausa or pausa_botao:
            self.som_controller.pause_music()
            return "pausa"
        elif morreu:
            self.som_controller.stop_music()
            self.som_controller.play_music(1)
            return "derrota"
        else:
            return "jogando"
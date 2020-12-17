from estado import Estado
from events_padrao import EventsPadrao
from texto import Texto
from fundo import Fundo
from botao import Botao
from botao_imagem import BotaoImagem
import pygame


class EstadoInicial(Estado):
    def __init__(self, jogador):
        super().__init__(jogador)
        self.__events_inicial = EventsPadrao()
        
        self.__nome_jogo1 = Texto("co", "Materials/Mario-Kart-DS.ttf", 50, self.WHITE, [22, 100])
        self.__nome_jogo2 = Texto("RUN", "Materials/Mario-Kart-DS.ttf", 60, self.WHITE, [79, 85])
        self.__nome_jogo3 = Texto("avirus", "Materials/Mario-Kart-DS.ttf", 50, self.WHITE, [209, 100])

        self.__imagem_regras = pygame.image.load("Materials/interrogacao.png").convert_alpha(self.tela.display)
        self.__fundo_regras = Fundo([340, 10, 50, 50], self.WHITE)
        self.__botao_regras = BotaoImagem(self.__imagem_regras, [345, 15], self.__fundo_regras, self.GREEN, self.DARK_GREEN, self.__events_inicial)
        
        self.__imagem_som = pygame.image.load("Materials/som.png").convert_alpha(self.tela.display)
        self.__fundo_som = Fundo([280, 10, 50, 50], self.WHITE)
        self.__botao_som = BotaoImagem(self.__imagem_som, [285, 15], self.__fundo_som, self.GREEN, self.DARK_GREEN, self.__events_inicial)
        
        self.__imagem_devs = pygame.image.load("Materials/devs.png").convert_alpha(self.tela.display)
        self.__fundo_devs = Fundo([220, 10, 50, 50], self.WHITE)
        self.__botao_devs = BotaoImagem(self.__imagem_devs, [225, 15], self.__fundo_devs, self.GREEN, self.DARK_GREEN, self.__events_inicial)

        self.__fundo_pontuacao = Fundo([20, 200, 360, 70], self.DARK_GREY)
        self.__texto_pontuacao = Texto(f"Recorde: {self.recordes_controller.primeiro()}", "Materials/Early GameBoy.ttf", 20, self.WHITE, [30, 220])

        self.__texto_recordes = Texto("Recordes", "Materials/Retro Gaming.ttf", 40, self.WHITE, [80, 310])
        self.__fundo_recordes = Fundo([20, 300, 360, 70], self.WHITE)
        self.__botao_recordes = Botao(self.__texto_recordes, self.__fundo_recordes, self.GREEN, self.DARK_GREEN, self.__events_inicial)
        
        self.__texto_play = Texto("PLAY", "Materials/Retro Gaming.ttf", 60, self.WHITE, [110, 397])
        self.__fundo_play = Fundo([20, 400, 360, 70], self.WHITE)
        self.__botao_play = Botao(self.__texto_play, self.__fundo_play, self.GREEN, self.DARK_GREEN, self.__events_inicial)

    def start(self):
        #Updates
        if not self.musica:
            self.som_controller.play_music(1)
            self.musica = True
        self.__events_inicial.check_events()
        play = self.__botao_play.update()
        regras = self.__botao_regras.update()
        recordes = self.__botao_recordes.update()
        som = self.__botao_som.update()
        devs = self.__botao_devs.update()

        # Draws
        self.tela.fill(self.GREY)
        self.__nome_jogo1.draw()
        self.__nome_jogo2.draw()
        self.__nome_jogo3.draw()
        self.__fundo_pontuacao.blitme()
        if len(self.recordes_controller.recordes) > 0:
            self.__texto_pontuacao.texto = str(f"Recorde: {self.recordes_controller.primeiro()['pontos']}")
        else:
            self.__texto_pontuacao.texto = str(f"Recorde:")
        self.__texto_pontuacao.draw()

        self.__botao_play.draw()
        self.__botao_regras.draw()
        self.__botao_som.draw()
        self.__botao_devs.draw()
        self.__botao_recordes.draw()

        if play:
            self.som_controller.stop_music()
            self.som_controller.play_music(0)
            return "jogando"
        elif regras:
            return "regras"
        elif recordes:
            return "recorde"
        elif som:
            return "som"
        elif devs:
            return "developers"
        else:
            return "inicial"

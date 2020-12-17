from estado import Estado
from texto import Texto
from fundo import Fundo
from botao_imagem import BotaoImagem
from events_padrao import EventsPadrao
import pygame


class EstadoRegras(Estado):
    def __init__(self):
        super().__init__()
        self.__events_regras = EventsPadrao()
        self.__texto_regras = Texto("Regras", "Materials/Early GameBoy.ttf", 50, self.BLACK, [60, 40])
        self.__imagem_botao_voltar = pygame.image.load("Materials/voltar.png").convert_alpha(self.tela.display)
        self.__fundo_voltar = Fundo([20, 510, 70, 70], self.WHITE)
        self.__botao_voltar = BotaoImagem(self.__imagem_botao_voltar, (25, 515), self.__fundo_voltar, self.GREEN, self.DARK_GREEN, self.__events_regras)
        self.__fundo_texto_regras = Fundo([20, 140, 360, 350], self.DARK_GREY)
        self.__imagem_regras = pygame.image.load("Materials/texto_regras.png").convert_alpha(self.tela.display)
        self.__rect_regras = (30, 150)

    def start(self):
        #Updates
        self.__events_regras.check_events()
        voltar = self.__botao_voltar.update()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_regras.draw()
        self.__fundo_texto_regras.blitme()
        self.tela.display.blit(self.__imagem_regras, self.__rect_regras)
        self.__botao_voltar.draw()
        
        if voltar:
            return "inicial"
        else:
            return "regras"

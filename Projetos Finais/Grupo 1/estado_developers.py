from estado import Estado
from texto import Texto
from fundo import Fundo
from botao_imagem import BotaoImagem
from events_padrao import EventsPadrao
import pygame


class EstadoDevelopers(Estado):
    def __init__(self):
        super().__init__()
        self.__events_developers = EventsPadrao()
        self.__texto_developers = Texto("Developers", "Materials/Early GameBoy.ttf", 38, self.BLACK, [15, 40])
        
        self.__fundo_texto_developers = Fundo([20, 140, 360, 350], self.DARK_GREY)
        self.__imagem_developers = pygame.image.load("Materials/texto_developers.png").convert_alpha(self.tela.display)
        self.__rect_developers = (30, 150)
        
        self.__imagem_botao_voltar = pygame.image.load("Materials/voltar.png").convert_alpha(self.tela.display)
        self.__fundo_voltar = Fundo([20, 510, 70, 70], self.WHITE)
        self.__botao_voltar = BotaoImagem(self.__imagem_botao_voltar, (25, 515), self.__fundo_voltar, self.GREEN, self.DARK_GREEN, self.__events_developers)


    def start(self):
        #Updates
        self.__events_developers.check_events()
        voltar = self.__botao_voltar.update()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_developers.draw()
        self.__fundo_texto_developers.blitme()
        self.tela.display.blit(self.__imagem_developers, self.__rect_developers)
        self.__botao_voltar.draw()
        
        if voltar:
            return "inicial"
        else:
            return "developers"

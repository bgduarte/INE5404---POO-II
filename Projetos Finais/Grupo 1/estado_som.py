from estado import Estado
from events_som import EventsSom
from texto import Texto
from fundo import Fundo
from botao import Botao
from botao_imagem import BotaoImagem
import pygame
from pygame_widgets import Slider


class EstadoSom(Estado):
    def __init__(self):
        super().__init__()
        self.__texto_som = Texto("Som", "Materials/Early GameBoy.ttf", 50, self.BLACK, [130, 40])
        
        self.__texto_musica = Texto("Volume música:", "Materials/Retro Gaming.ttf", 25, self.WHITE, [20, 150])
        self.__texto_efeitos = Texto("Volume efeitos:", "Materials/Retro Gaming.ttf", 25, self.WHITE, [20, 300])
        
        self.__slider_musica = Slider(self.tela.display, 20, 230, 300, 20, min=0, max=1, step=0.1, handleColour=self.GREEN)
        self.__slider_musica.setValue(self.som_controller.volume_atual_music)
        self.__slider_sons = Slider(self.tela.display, 20, 380, 300, 20, min=0, max=1, step=0.1, handleColour=self.GREEN)
        self.__slider_sons.setValue(self.som_controller.volume_atual_sound)
        self.__sliders = [self.__slider_musica, self.__slider_sons]
        self.__events_som = EventsSom(self.__sliders)

        self.__numero_musica = Texto("", "Materials/Retro Gaming.ttf", 25, self.WHITE, [335, 225])
        self.__numero_sons = Texto("", "Materials/Retro Gaming.ttf", 25, self.WHITE, [335, 375])
        
        self.__imagem_botao_voltar = pygame.image.load("Materials/voltar.png").convert_alpha(self.tela.display)
        self.__fundo_voltar = Fundo([20, 510, 70, 70], self.WHITE)
        self.__botao_voltar = BotaoImagem(self.__imagem_botao_voltar, (25, 515), self.__fundo_voltar, self.GREEN, self.DARK_GREEN, self.__events_som)
        
        self.__texto_vol_padrao = Texto("Volume Padrão", "Materials/Retro Gaming.ttf", 27, self.BLACK, [125, 525])
        self.__fundo_vol_padrao = Fundo([110, 510, 270, 70], self.WHITE)
        self.__botao_vol_padrao = Botao(self.__texto_vol_padrao, self.__fundo_vol_padrao, self.GREEN, self.DARK_GREEN, self.__events_som)


    def start(self):
        #Updates
        self.__events_som.check_events()
        self.som_controller.set_volume_music(self.__slider_musica.getValue())
        self.som_controller.set_volume_sounds(self.__slider_sons.getValue())
        voltar = self.__botao_voltar.update()
        padrao = self.__botao_vol_padrao.update()
        if padrao:
            self.som_controller.set_volume_padrao()
            self.__slider_musica.setValue(self.som_controller.volume_atual_music)
            self.__slider_sons.setValue(self.som_controller.volume_atual_sound)
        
        porcentagem_musica = self.__slider_musica.getValue() * 100
        porcentagem_sons = self.__slider_sons.getValue() * 100
        self.__numero_musica.texto = str(int(porcentagem_musica)) + "%"
        self.__numero_sons.texto = str(int(porcentagem_sons)) + "%"

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_som.draw()
        self.__texto_musica.draw()
        self.__texto_efeitos.draw()
        self.__slider_musica.draw()
        self.__slider_sons.draw()
        self.__numero_musica.draw()
        self.__numero_sons.draw()
        self.__botao_voltar.draw()
        self.__botao_vol_padrao.draw()

        if voltar:
            return "inicial"
        else:
            return "som"
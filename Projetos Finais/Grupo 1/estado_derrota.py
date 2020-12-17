from estado import Estado
from events_derrota import EventsDerrota
from texto import Texto
from fundo import Fundo
from botao import Botao
from botao_imagem import BotaoImagem
import pygame
from pygame_widgets import TextBox


class EstadoDerrota(Estado):
    def __init__(self, jogador, obstaculo_controller, efeito_controller):
        super().__init__(jogador, obstaculo_controller, efeito_controller)
        self.__recorde_salvo = False

        self.__texto_derrota = Texto("Derrota", "Materials/Early GameBoy.ttf", 50, self.BLACK, [30, 40])
        
        self.__fundo_pontuacao = Fundo([20, 140, 360, 70], self.DARK_GREY)
        self.__texto_pontuacao = Texto(f"Pontos: {self.pontuacao.pontos}", "Materials/Early GameBoy.ttf", 20, self.WHITE, [30, 160])

        self.__nome = TextBox(self.tela.display, 20, 250, 280, 70, borderColour=(0, 0, 0), textColour=(0, 0, 0), radius=10, borderThickness=5)
        self.__nome.font = pygame.font.Font("Materials/Retro Gaming.ttf", 30)
        self.__texto_recorde = Texto("Insira seu nome e clique em salvar.", "Materials/Retro Gaming.ttf", 12, self.BLACK, [25, 325])

        self.__events_derrota = EventsDerrota(self.__nome)
        
        self.__imagem_botao_salvar = pygame.image.load("Materials/disquete.png").convert_alpha(self.tela.display)
        self.__fundo_salvar = Fundo([310, 250, 70, 70], self.WHITE)
        self.__botao_salvar = BotaoImagem(self.__imagem_botao_salvar, (315, 255), self.__fundo_salvar, self.GREEN, self.DARK_GREEN, self.__events_derrota)
        
        self.__texto_jogar_novamente = Texto("Jogar novamente", "Materials/Retro Gaming.ttf", 30, self.WHITE, [40, 395])
        self.__fundo_jogar_novamente = Fundo([20, 380, 360, 70], self.WHITE)
        self.__botao_jogar_novamente = Botao(self.__texto_jogar_novamente, self.__fundo_jogar_novamente, self.GREEN, self.DARK_GREEN, self.__events_derrota)
        
        self.__texto_menu = Texto("Menu", "Materials/Retro Gaming.ttf", 40, self.WHITE, [135, 490])
        self.__fundo_menu = Fundo([20, 480, 360, 70], self.WHITE)
        self.__botao_menu = Botao(self.__texto_menu, self.__fundo_menu, self.GREEN, self.DARK_GREEN, self.__events_derrota)  

    def salvar_recorde(self):
        if self.__nome.getText() != "":
            if len(self.__nome.getText()) > 10:
                self.__texto_recorde.texto = "Digite um nome menor, limite 10 caracteres."
            elif not self.__recorde_salvo:
                msg, salvo = self.recordes_controller.inclui_recorde(self.__nome.getText(), self.pontuacao.pontos)
                self.__texto_recorde.texto = msg
                self.__recorde_salvo = salvo
            else:
                self.__texto_recorde.texto = "Só é possível salvar o recorde uma vez."
        else:
            self.__texto_recorde.texto = "Digite um nome."

        self.__nome.setText("")
        self.__nome.cursorPosition = 0

    def start(self):
        #Updates
        self.__events_derrota.check_events()
        jogar_novamente = self.__botao_jogar_novamente.update()
        menu_derrota = self.__botao_menu.update()

        salvar_recorde = self.__botao_salvar.update()
        if salvar_recorde:
            self.salvar_recorde()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_derrota.draw()
        self.__fundo_pontuacao.blitme()

        self.__texto_pontuacao.texto = str(f"Pontos: {self.pontuacao.pontos}")
        self.__texto_pontuacao.draw()

        self.__nome.draw()
        self.__botao_salvar.draw()
        self.__texto_recorde.draw()

        self.__botao_jogar_novamente.draw()
        self.__botao_menu.draw()

        if jogar_novamente:
            self.__recorde_salvo = False
            self.__texto_recorde.texto = "Insira seu nome e clique em salvar."
            self.pontuacao.zerar()
            self.velocidade_controller.zerar()
            self.fases_controller.zerar()
            self.jogador.reset()
            self.obstaculo_controller.zerar()
            self.efeito_controller.zerar()
            self.som_controller.stop_music()
            self.som_controller.play_music(0)
            return "jogando"
        elif menu_derrota:
            self.__recorde_salvo = False
            self.__texto_recorde.texto = "Insira seu nome e clique em salvar."
            self.pontuacao.zerar()
            self.velocidade_controller.zerar()
            self.fases_controller.zerar()
            self.jogador.reset()
            self.obstaculo_controller.zerar()
            self.efeito_controller.zerar()
            return "inicial"
        else:
            return "derrota"
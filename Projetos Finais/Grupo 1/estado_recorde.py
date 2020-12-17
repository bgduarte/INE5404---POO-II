from estado import Estado
from botao import Botao
from texto import Texto
from fundo import Fundo
from botao_imagem import BotaoImagem
from events_padrao import EventsPadrao
import pygame


class EstadoRecorde(Estado):
    def __init__(self):
        super().__init__()
        self.__events_recorde = EventsPadrao()
        self.__texto_recordes = Texto("Recordes", "Materials/Early GameBoy.ttf", 50, self.BLACK, [5, 40])
        self.__fundo_texto_recorde = Fundo([20, 140, 360, 350], self.DARK_GREY)
        self.__imagem_botao_voltar = pygame.image.load("Materials/voltar.png").convert_alpha(self.tela.display)
        self.__fundo_voltar = Fundo([20, 510, 70, 70], self.WHITE)
        self.__botao_voltar = BotaoImagem(self.__imagem_botao_voltar, (25, 515), self.__fundo_voltar, self.GREEN, self.DARK_GREEN, self.__events_recorde)
        self.__imagem_botao_limpar = pygame.image.load("Materials/lixeira.png").convert_alpha(self.tela.display)
        self.__fundo_limpar = Fundo([310, 510, 70, 70], self.WHITE)
        self.__botao_limpar = BotaoImagem(self.__imagem_botao_limpar, (315, 515), self.__fundo_limpar, self.GREEN, self.DARK_GREEN, self.__events_recorde)
        self.__cabecalho_nomes = "Nomes:"
        self.__texto_lista_nomes = [Texto(self.__cabecalho_nomes, "Materials/Retro Gaming.ttf", 18, self.WHITE, [40, 150])]
        self.__cabecalho_pontos = "Pontos:"
        self.__texto_lista_pontos = [Texto(self.__cabecalho_pontos, "Materials/Retro Gaming.ttf", 18, self.WHITE, [230, 150])]
        for i in range(15):
            cores = [self.YELLOW, self.SILVER, self.BRONZE, self.WHITE]
            cor = None
            if i == 0:
                cor = cores[0]
            elif i == 1:
                cor = cores[1]
            elif i == 2:
                cor = cores[2]
            else:
                cor = cores[3]
            self.__texto_lista_nomes.append(Texto(f"{i + 1} - ", "Materials/Retro Gaming.ttf", 15, cor, [40, 180 + 20 * i]))
            self.__texto_lista_pontos.append(Texto("", "Materials/Retro Gaming.ttf", 15, cor, [230, 180 + 20 * i]))

    def listar_recordes(self):
        recordes = self.recordes_controller.recordes
        limite = 15
        if len(recordes) < 15:
            limite = len(recordes)
            
        for i in range(limite):
            self.__texto_lista_nomes[i+1].texto = f'{i + 1} - {recordes[i]["nome"]}'
            self.__texto_lista_pontos[i+1].texto = f'{recordes[i]["pontos"]}'

    def limpar_lista_recordes(self):
        for i in range(15):
            self.__texto_lista_nomes[i+1].texto = f"{i + 1} - "
            self.__texto_lista_pontos[i+1].texto = ""

    def start(self):
        #Updates
        self.__events_recorde.check_events()
        self.listar_recordes()
        voltar = self.__botao_voltar.update()
        limpar = self.__botao_limpar.update()
        
        if limpar:
            self.recordes_controller.limpar_recordes()
            self.limpar_lista_recordes()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_recordes.draw()
        self.__fundo_texto_recorde.blitme()
        self.__botao_voltar.draw()
        self.__botao_limpar.draw()

        for i in range(16):
            self.__texto_lista_nomes[i].draw()
            self.__texto_lista_pontos[i].draw()
        
        if voltar:
            return "inicial"
        else:
            return "recorde"

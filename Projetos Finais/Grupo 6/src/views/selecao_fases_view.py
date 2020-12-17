import os
from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from src.config.menu_config_loader import MenuConfigLoader
from src.views.widgets.botao_fase import BotaoFase
from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.input_jogador import InputJogador
from src.views.widgets.titulo_janela import TituloJanela


class SelecaoFasesView(QWidget):
    sinal_fase = pyqtSignal(str, int)
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        titulo = TituloJanela("Selecione a fase")
        titulo.adicionar_ao_layout(self.__layout)

        self.__input_jogador =  InputJogador()
        self.__input_jogador.adicionar_ao_layout(self.__layout)

        fases_layout = QGridLayout()
        nome_imagens = sorted(os.listdir(os.path.join(self.__config.diretorio_assets, "thumbnail fases")))
        botoes = []
        for nome in nome_imagens:
            botao = BotaoFase(nome, nome_imagens.index(nome) + 1)
            botoes.append(botao)
        botoes[0].clicked.connect(self.__selecionar_fase1)
        botoes[1].clicked.connect(self.__selecionar_fase2)
        botoes[2].clicked.connect(self.__selecionar_fase3)
        botoes[3].clicked.connect(self.__selecionar_fase4)
        botoes[4].clicked.connect(self.__selecionar_fase5)
        botoes[5].clicked.connect(self.__selecionar_fase6)
        fases_layout.addWidget(botoes[0], 0, 0)
        fases_layout.addWidget(botoes[1], 0, 1)
        fases_layout.addWidget(botoes[2], 0, 2)
        fases_layout.addWidget(botoes[3], 1, 0)
        fases_layout.addWidget(botoes[4], 1, 1)
        fases_layout.addWidget(botoes[5], 1, 2)
        self.__layout.addLayout(fases_layout)

        botao_voltar = BotaoPadrao("Voltar")
        botao_voltar.clicked.connect(self.__voltar)
        botao_voltar.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __selecionar_fase1(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 0)

    def __selecionar_fase2(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 1)

    def __selecionar_fase3(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 2)

    def __selecionar_fase4(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 3)

    def __selecionar_fase5(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 4)

    def __selecionar_fase6(self):
        self.sinal_fase.emit(self.__obter_nome_jogador(), 5)

    def __obter_nome_jogador(self):
        try:
            nome = self.__input_jogador.text()
            assert nome is not ''
        except AssertionError:
            return "Jogador desconhecido"
        else:
            return nome

    def __voltar(self):
        self.sinal_voltar.emit()

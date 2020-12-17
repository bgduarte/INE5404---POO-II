import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.imagem_central import ImagemCentral
from src.views.widgets.titulo_janela import TituloJanela


# A view herda de QWidget do PyQt5 para ser usada na janela principal
class MainMenuView(QWidget):
    sinal_jogar = pyqtSignal()
    sinal_leaderboard = pyqtSignal()
    sinal_ajuda = pyqtSignal()

    # Criamos o layout dessa view
    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    # Adicionamos os widgets customizados ao layout
    # Cada botão está conectado à uma função que emite um sinal que é recebido
    # e tratado pelo controller
    def mostra_view(self):
        imagem_central = ImagemCentral()
        imagem_central.adicionar_ao_layout(self.__layout)

        botao_jogar = BotaoPadrao("Jogar")
        botao_jogar.clicked.connect(self.__jogar)
        botao_jogar.adicionar_ao_layout(self.__layout)

        botao_leaderboard = BotaoPadrao("Leaderboard")
        botao_leaderboard.clicked.connect(self.__leaderboard)
        botao_leaderboard.adicionar_ao_layout(self.__layout)

        botao_ajuda = BotaoPadrao("Ajuda")
        botao_ajuda.clicked.connect(self.__ajuda)
        botao_ajuda.adicionar_ao_layout(self.__layout)

        botao_sair = BotaoPadrao("Sair")
        botao_sair.clicked.connect(self.__sair)
        botao_sair.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __jogar(self):
        self.sinal_jogar.emit()

    def __leaderboard(self):
        self.sinal_leaderboard.emit()

    def __ajuda(self):
        self.sinal_ajuda.emit()

    def __sair(self):
        sys.exit()

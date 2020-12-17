import os
from PyQt5.Qt import pyqtSignal, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from src.config.menu_config_loader import MenuConfigLoader
from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.titulo_janela import TituloJanela


class AjudaView(QWidget):
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        titulo = TituloJanela("Ajuda")
        titulo.adicionar_ao_layout(self.__layout)

        pixmap = QPixmap(os.path.join(self.__config.diretorio_assets, "ajuda.png"))
        imagem = QLabel()
        imagem.setPixmap(pixmap)
        self.__layout.addWidget(imagem, alignment = Qt.AlignCenter)

        botao_voltar = BotaoPadrao("Voltar")
        botao_voltar.clicked.connect(self.__voltar)
        botao_voltar.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __voltar(self):
        self.sinal_voltar.emit()

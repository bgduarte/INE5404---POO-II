from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

from src.config.menu_config_loader import MenuConfigLoader


class InputJogador(QLineEdit):
    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.setFixedSize(self.__config.width_input_jogador, self.__config.height_input_jogador)
        self.setFont(QFont(self.__config.fonte_input_jogador, self.__config.tamanho_fonte_input_jogador))
        self.setAlignment(Qt.AlignCenter)
        self.setPlaceholderText("Digite o nome do jogador")

    def adicionar_ao_layout(self, layout):
        layout.addWidget(self, alignment = Qt.AlignHCenter)

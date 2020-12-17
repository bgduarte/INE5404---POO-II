from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from src.config.menu_config_loader import MenuConfigLoader


class TituloJanela(QLabel):
    def __init__(self, texto):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.setText(texto)
        self.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))

    def adicionar_ao_layout(self, layout):
        layout.addWidget(self, alignment = Qt.AlignHCenter | Qt.AlignTop)

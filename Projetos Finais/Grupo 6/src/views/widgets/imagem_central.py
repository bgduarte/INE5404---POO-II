import os
from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from src.config.menu_config_loader import MenuConfigLoader


class ImagemCentral(QLabel):
    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__pixmap = QPixmap(os.path.join(self.__config.diretorio_assets, "menu principal/centro.png"))
        self.setPixmap(self.__pixmap)

    def adicionar_ao_layout(self, layout):
        layout.addWidget(self, alignment = Qt.AlignCenter)

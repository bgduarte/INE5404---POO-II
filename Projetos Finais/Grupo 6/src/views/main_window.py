import os
from PyQt5.Qt import QPixmap, QPainter
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src.config.menu_config_loader import MenuConfigLoader


# A janela principal herda de QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        #Configurações da janela
        self.setStyleSheet(self.__config.stylesheet)
        self.setFixedSize(self.__config.width_janela, self.__config.height_janela)
        self.setWindowIcon(QIcon(os.path.join(self.__config.diretorio_assets, "icon","icon.png")))
        self.setWindowTitle("Blockfiesta!")

    #Reescrever o paintEvent da classe QMainWindow, para a
    #janela ser criada com o fundo que queremos
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap(os.path.join(self.__config.diretorio_assets, "menu principal", "fundo.png")))
        super().paintEvent(event)

import os
from PyQt5.Qt import QFont
from PyQt5.QtWidgets import QPushButton
from sys import platform

from src.config.menu_config_loader import MenuConfigLoader


class BotaoFase(QPushButton):
    def __init__(self, imagem, numero_fase):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__diretorio = os.path.join(self.__config.diretorio_assets, "thumbnail fases", imagem)
        self.setFixedSize(self.__config.width_fases, self.__config.height_fases)
        self.setFont(QFont(self.__config.fonte_botoes_fase, self.__config.tamanho_fonte_botoes_fase))
        self.setText(f"Fase {numero_fase}")
        # Windows sendo windows...
        if platform == "win32":
            self.setStyleSheet("""BotaoFase{ border-style: outset; background-color: #14AE12;
            border-color: #14AE12; border-radius: 20px; border-width: 6px; font-color: black;}
            BotaoFase:hover { border-color: #28C226; background-color: #28C226; }
            BotaoFase:pressed { border-color: #009A00; background-color: #009A00; }""")
        else:
            self.setStyleSheet("BotaoFase{ " +
                           f"background-image: url({self.__diretorio}); " +
                           "color: darkgreen; border-style: outset; border-color: #14AE12; border-radius: 20px; border-width: 6px; " +
                           "} BotaoFase:hover { border-color: #28C226; } BotaoFase:pressed { border-color: #009A00; }")


from PyQt5.QtWidgets import QPushButton

from src.config.menu_config_loader import MenuConfigLoader


class BotaoFase(QPushButton):
    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.setFixedSize(self.__config.width_fases, self.__config.height_fases)

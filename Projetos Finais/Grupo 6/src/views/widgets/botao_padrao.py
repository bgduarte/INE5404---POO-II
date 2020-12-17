from PyQt5.Qt import QFont, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton

from src.config.menu_config_loader import MenuConfigLoader


# Herda da classe QPushButton do PyQt5 e inicializa o objeto com os valores que queremos
class BotaoPadrao(QPushButton):
    def __init__(self, texto):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        self.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        self.setText(texto)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    # Adiciona ao layout com o alinhamento desejado
    def adicionar_ao_layout(self, layout):
        layout.addWidget(self, alignment = Qt.AlignHCenter | Qt.AlignBottom)

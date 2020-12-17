import pygame
import pygame_menu
from sys import platform

from src.config.menu_pause_config_loader import MenuPauseConfigLoader
from src.game.interfaces.interface_menu_pause import IMenuPause


class MenuPause(IMenuPause):
    def __init__(self, screen):
        self.__config = MenuPauseConfigLoader()
        self.__screen = screen
        self.__tema = self.__criar_tema()
        self.__menu = pygame_menu.Menu(self.__screen.get_height(), self.__screen.get_width(), 'Jogo pausado', theme = self.__tema)
        self.__menu.add_button("Continuar", self.continuar)
        self.__menu.add_button("Menu principal", self.voltar_menu_principal)
        self.__menu.add_button("Sair", self.sair_do_jogo)
        self.__voltar = False

    def show(self):
        self.__menu.enable()
        self.__menu.mainloop(self.__screen)

    def continuar(self):
        self.hide()

    def hide(self):
        self.__menu.disable()

    def sair_do_jogo(self):
        exit()

    #Não gosto dessa implementação mas por hora vai funcionar
    def voltar_menu_principal(self):
        self.__voltar = True
        self.hide()

    def __criar_tema(self):
        # Windows sendo windows...
        if platform == "win32":
            tema = pygame_menu.themes.Theme(background_color = self.__config.cor_fundo,
                                        title_font = "tahoma",
                                        title_font_size = 72,
                                        title_font_color = self.__config.cor_fonte_titulo,
                                        title_background_color = self.__config.cor_fundo_titulo,
                                        menubar_close_button = False,
                                        widget_alignment = pygame_menu.locals.ALIGN_CENTER,
                                        widget_font = "tahoma",
                                        widget_font_size = 64,
                                        widget_font_color = self.__config.cor_fonte_botoes,
                                        widget_margin = self.__config.espacamento)
        else:
            tema = pygame_menu.themes.Theme(background_color = self.__config.cor_fundo,
                                            title_font = self.__config.fonte_titulo,
                                            title_font_size = self.__config.tamanho_fonte_titulo,
                                            title_font_color = self.__config.cor_fonte_titulo,
                                            title_background_color = self.__config.cor_fundo_titulo,
                                            menubar_close_button = False,
                                            widget_alignment = pygame_menu.locals.ALIGN_CENTER,
                                            widget_font = self.__config.fonte_botoes,
                                            widget_font_size = self.__config.tamanho_fonte_botoes,
                                            widget_font_color = self.__config.cor_fonte_botoes,
                                            widget_margin = self.__config.espacamento)
        return tema

    @property
    def voltar(self):
        return self.__voltar

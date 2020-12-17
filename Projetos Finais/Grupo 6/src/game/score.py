import datetime


class Score:
    def __init__(self, tempo, fase, jogador):
        self.__tempo = tempo
        self.__fase = fase
        self.__jogador = jogador

    def to_dict(self):
        return self.__tempo

    def to_string(self):
        return f"{self.__jogador} completou a fase {self.__fase} em {self.__tempo} segundos"

    @property
    def jogador(self):
        return self.__jogador

    @property
    def fase(self):
        return self.__fase

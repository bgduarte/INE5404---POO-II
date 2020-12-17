import json
import os

from src.game.score import Score


class DAO:
    def __init__(self):
        self.__datasource = os.path.join(os.getenv("PYTHONPATH"), "scores/scores.json")
        self.__cache = {}
        self.__load()

    def __dump(self):
        f = open(self.__datasource, 'w')
        json.dump(self.__cache, f, indent = 4)

    def __load(self):
        try:
            f = open(self.__datasource, 'r')
        except FileNotFoundError:
            self.__dump()
            self.__load()
        else:
            self.__cache = json.load(f)

    def add(self, score: Score):
        if isinstance(score, Score):
            print ('isinstance')
            if score.jogador not in self.__cache.keys():
                print ('Dentro do if')
                self.__cache[score.jogador] = {}
                for i in range(1, 7):
                    print ('Fazendo laço for')
                    self.__cache[score.jogador][f"fase{i}"] = []
            self.__cache[score.jogador][f"fase{score.fase}"].append(score.to_dict())
            self.__dump()
            #Persistência: Este Data-Access Object realizará a comparação da pontuação recebida com os recordes e,se necessária,
            # guardará o novo recorde de tempo da fase em um arquivo json.

    def melhor_tempo_fase(self, fase):
        #pode ser qualquer número suficientemente grande
        minimo = 100000
        for key in self.__cache.keys():
            for tempo in self.__cache[key][f"fase{fase}"]:
                if tempo < minimo:
                    jogador = key
                    minimo = tempo
        return Score(minimo, fase, jogador)

    def atualizar(self):
        self.__load()

    @property
    def cache(self):
        return self.__cache

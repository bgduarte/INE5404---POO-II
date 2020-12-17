from recorde_dao import RecordeDAO
from singleton import Singleton


class RecordesController(metaclass=Singleton):
    def __init__(self):
        self.__recorde_dao = RecordeDAO()

    def inclui_recorde(self, nome, pontos):
        msg = "Recorde salvo com sucesso!"
        salvo = False
        if self.__recorde_dao.get(nome) == None:
            self.__recorde_dao.add(nome, pontos)
            salvo = True
        else:
            salvo = self.__recorde_dao.replace(nome, pontos)
        if not salvo:
            msg = "Recorde mais baixo que o existente."
        return msg, salvo

    def limpar_recordes(self):
        self.__recorde_dao.remove_all()

    def primeiro(self):
        return self.__recorde_dao.get_first()

    @property
    def recordes(self):
        return self.__recorde_dao.get_all()
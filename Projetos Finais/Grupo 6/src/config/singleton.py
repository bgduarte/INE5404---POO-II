# Para garantir que haja apenas uma instância da classe reescrevemos o método new do objeto
# ConfigLoaders herdarão dessa classe, então sempre que um objeto for criado o método __new__ será chamado
class Singleton(object):
    __instance = None

    # Se não tiver uma instância da classe criada, cria uma,
    # se tiver, retorna essa instância
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

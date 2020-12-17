import pickle


class VolumeDAO:
    def __init__(self, datasource="volume.pkl"):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        data = open(self.__datasource, "wb")
        pickle.dump(self.__object_cache, data)
        data.close()

    def __load(self):
        data = open(self.__datasource, "rb")
        self.__object_cache = pickle.load(data)
        data.close()

    def get_all(self):
        return self.__object_cache

    def get_volume_music(self):
        return self.__object_cache["music"]

    def get_volume_sound(self):
        return self.__object_cache["sound"]

    def set_volume_music(self, volume):
        self.__object_cache["music"] = volume
        self.__dump()

    def set_volume_sound(self, volume):
        self.__object_cache["sound"] = volume
        self.__dump()

    def set_volume_padrao(self):
        self.__object_cache = {"music": 0.5,"sound": 0.5}
        self.__dump()

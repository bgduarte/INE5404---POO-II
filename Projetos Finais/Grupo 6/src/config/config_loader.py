import os
from abc import ABC, abstractmethod


class ConfigLoader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @property
    def diretorio_assets(self):
        return os.path.join(os.getenv("PYTHONPATH"), "assets")

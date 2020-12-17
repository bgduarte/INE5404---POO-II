from abc import ABC, abstractmethod


class IItem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def usar(self):
        pass

    @property
    @abstractmethod
    def material(self):
        pass

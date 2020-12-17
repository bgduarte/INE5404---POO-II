import sys
import pygame
from abc import ABC, abstractmethod


class Events(ABC):
    @abstractmethod
    def check_events(self):
        pass

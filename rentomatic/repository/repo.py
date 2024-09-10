from abc import ABCMeta, abstractmethod
from typing import List

from rentomatic.domain.room import Room


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def list(self, filters: dict = None) -> List[Room]:
        pass
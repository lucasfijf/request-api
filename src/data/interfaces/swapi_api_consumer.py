from abc import ABC, abstractmethod
from typing import Type, Tuple, Dict
from requests import Request

class SwapiApiConsumerInterface(ABC):
    """Swapi api consumer interface"""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        raise NotImplementedError()
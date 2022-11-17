from abc import ABC, abstractmethod
from typing import Type, Tuple, Dict
from requests import Request

class SwapiApiConsumerInterface(ABC):
    """Swapi api consumer interface"""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Must implement"""
        raise NotImplementedError()

    @abstractmethod
    def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        """Must implement"""
        raise NotImplementedError()

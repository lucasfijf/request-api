from abc import ABC, abstractmethod
from typing import Dict, List

class StarshipInformationCollectorInterface(ABC):
    """Starship information collector interface"""

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> List[Dict]:
        """Must implement"""

        raise NotImplementedError()

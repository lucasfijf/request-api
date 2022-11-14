from abc import ABC, abstractmethod
from typing import Dict, List

class StarshipsListCollectorInterface(ABC):
    """Starships collector interface"""

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        """Must implement"""

        raise NotImplementedError()
        
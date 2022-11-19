from typing import Dict
from abc import ABC, abstractmethod

class ControllersInterface(ABC):
    """Interface to controllers"""

    @abstractmethod
    def handle(self, http_request: Dict):
        """Method to handle request"""

        raise NotImplementedError()

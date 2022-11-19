from typing import Type, Dict
from src.domain.usecases.starships_list_collector import StarshipsListCollectorInterface
from src.presenters.interfaces import ControllersInterface

class StarshipsListCollectorController(ControllersInterface):
    """List starships controller"""

    def __init__(self, starships_list_collector: Type[StarshipsListCollectorInterface]) -> None:
        self.__use_case = starships_list_collector

    def handle(self, http_request: Dict) -> Dict:
        """List collector handle"""

        page = http_request["query_params"]["page"]
        starships_list = self.__use_case.list(page)
        http_response = {"status_code": 200, "data": starships_list}

        return http_response

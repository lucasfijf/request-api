from typing import Dict, Type
from src.presenters.interfaces import ControllersInterface
from src.domain.usecases.starship_information_collector import StarshipInformationCollectorInterface

class StarshipInformationCollectorController(ControllersInterface):
    """Controller to starship information collector"""

    def __init__(self, starship_information_collector: Type[StarshipInformationCollectorInterface]) -> None:
        self.__use_case = starship_information_collector

    def handle(self, http_request: Dict):
        """Handler to information collector controller"""

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__use_case.find_starship(starship_id, time)
        http_response = {"status_code": 200, "data": starship_information}

        return http_response

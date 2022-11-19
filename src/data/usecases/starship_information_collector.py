from typing import Type, Dict
from src.domain.usecases.starship_information_collector import StarshipInformationCollectorInterface
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.errors import HttpUnprocessableEntityError

class StarshipInformationCollector(StarshipInformationCollectorInterface):
    """Starship information collector usecase"""

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starship(self, starship_id: int, time: str) -> Dict:
        """Find starship information
        :param - starship_id: id of the starship
               - time: time in hours
        :return - dictionary with starship information
        """

        starship_information = self.__search_starship(starship_id)
        mglt = starship_information["MGLT"]
        distance_traveled = self.__calculate_distance_traveled_to_spaceship(mglt, time)
        formatted_response = self.__format_response(starship_information, distance_traveled)

        return formatted_response

    def __search_starship(self, starship_id: int) -> Dict:
        """Get starship and validate information
        :param - starship_id: id of the starship
        :return - dictionary with starship information from API
        """

        api_response = self.__api_consumer.get_starship_information(starship_id)

        if api_response.response["MGLT"] == "unknown":
            raise HttpUnprocessableEntityError("Unprocessable information for selected starship")

        return api_response.response

    @classmethod
    def __calculate_distance_traveled_to_spaceship(cls, mglt: str, time: str) -> int:
        """Algorithm to calculate distance traveled
        :param - mglt: string with max number of megalights for the starship
               - time: time in hours
        :return - distance traveled in megalights
        """

        distance_traveled = int(mglt) * int(time)

        return distance_traveled

    @classmethod
    def __format_response(cls, starship_information: Dict, distance_traveled: int) -> Dict:
        return {
            "starship": starship_information["name"],
            "model": starship_information["model"],
            "manufacturer": starship_information["manufacturer"],
            "max_atmosphering_speed": starship_information["max_atmosphering_speed"],
            "MGLT": starship_information["MGLT"],
            "distance_traveled": str(distance_traveled) + " ML"
        }

from typing import Type, Dict, List
from src.domain.usecases import StarshipsListCollectorInterface
from src.data.interfaces import SwapiApiConsumerInterface

class StarshipsListCollector(StarshipsListCollectorInterface):
    """Starships collector usecase"""

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        starships_formatted_list = self.__format_api_response(response.response["results"])

        return starships_formatted_list
    
    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        starships_formatted_list = []

        for starship in results:
            starships_formatted_list.append(
                {
                    "id": starship["url"].split("/")[-2],
                    "name": starship["name"],
                    "model": starship["model"],
                    "max_atmosphering_speed": starship["max_atmosphering_speed"],
                    "hyperdrive_rating": starship["hyperdrive_rating"],
                    "MGLT": starship["MGLT"],
                }
            )
        
        return starships_formatted_list
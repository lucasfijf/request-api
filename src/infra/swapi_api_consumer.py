from typing import Type, Tuple, Dict
from collections import namedtuple
import requests
from requests import Request
from src.errors import HttpRequestError
from src.data.interfaces import SwapiApiConsumerInterface

class SwapiApiConsumer:
    """Class to consume swapi api with http requests"""

    def __init__(self) -> None:
        self.get_starships_response = namedtuple("GET_Starships", "status_code, request, response")

    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Request starships in pagination
        :param - page: int with page navigation
        :return - tuple with status_code, request, response attributes
        """
        request = requests.Request(
            method="GET",
            url="https://swapi.dev/api/starships",
            params={"page": page}
        )
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        if status_code >= 200 and status_code <= 299:
            return self.get_starships_response(
                status_code=status_code,
                request=request,
                response=response.json()
            )

        raise HttpRequestError(
            message=response.json()["detail"],
            status_code=status_code
        )

    def __send_http_request(self, request_prepared: Type[Request]) -> any:
        """Prepare a session and send HTTP request
        :param - request_prepared: request object with all params
        :return - http response raw
        """
        http_session = requests.Session()
        response = http_session.send(request_prepared)
        return response

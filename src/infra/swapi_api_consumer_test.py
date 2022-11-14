from src.errors import HttpRequestError
from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships(requests_mock):
    """Testing get_starships method"""

    requests_mock.get("https://swapi.dev/api/starships", status_code=200, json={"results": [{}]})
    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    get_api = swapi_api_consumer.get_starships(page)

    assert get_api.request.method == "GET"
    assert get_api.request.url == "https://swapi.dev/api/starships"
    assert get_api.request.params == {"page": page}
    assert get_api.status_code == 200
    assert get_api.response["results"]

def test_get_starships_http_error(requests_mock):
    """Testing get_starships http error"""

    requests_mock.get("https://swapi.dev/api/starships", status_code=404, json={"detail": "something"})
    swapi_api_consumer = SwapiApiConsumer()
    page = 100

    try:
        get_api = swapi_api_consumer.get_starships(page)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
        
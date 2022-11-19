from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpy
from .starship_information_collector import StarshipInformationCollector

def test_find_starship():
    """Testing find_starship method"""

    api_consumer = SwapiApiConsumerSpy()
    starship_information_collector = StarshipInformationCollector(api_consumer)
    starship_id = 9
    time = 4

    response = starship_information_collector.find_starship(starship_id, time)

    assert api_consumer.get_starship_information_attributes["starship_id"] == starship_id
    assert isinstance(response, dict)
    assert "MGLT" in response
    assert "distance_traveled" in response

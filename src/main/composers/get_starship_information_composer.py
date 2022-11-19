from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.starship_information_collector import StarshipInformationCollector
from src.presenters.controllers.starship_information_collector_controller import StarshipInformationCollectorController

def get_starship_information_composer():
    """Composer"""

    infra = SwapiApiConsumer()
    usecase = StarshipInformationCollector(infra)
    controller = StarshipInformationCollectorController(usecase)

    return controller

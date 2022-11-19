from typing import Type, Dict
from src.errors import HttpRequestError, HttpUnprocessableEntityError

def handle_errors(error: Type[Exception]) -> Dict:
    """Handler to treat exception cases
    :param - error: exception
    :return: dict with data and status code
    """

    if isinstance(error, HttpRequestError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }

    if isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }

    return {
        "data": {"error": str(error)},
        "status_code": 500
    }

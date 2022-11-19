from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.validators.get_starship_information_validator import get_information_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_information_composer import get_starship_information_composer
from src.presenters.errors.error_controller import handle_errors

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: Request) -> JSONResponse:
    """Get starships in pagination route"""

    response = None
    controller = get_starships_in_pagination_composer()

    try:
        get_pagination_validator(request)
        response = await request_adapter(request, controller.handle)
    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )

@starships_routes.get("/api/starships/information")
async def get_starship_information(request: Request) -> JSONResponse:
    """Get starship information route"""

    response = None
    controller = get_starship_information_composer()

    try:
        await get_information_validator(request)
        response = await request_adapter(request, controller.handle)
    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )

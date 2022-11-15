from fastapi import APIRouter, Request
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters.request_adapter import request_adapter

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: Request):
    """Get starships in pagination route"""

    get_pagination_validator(request)
    await request_adapter(request, print)
    return {"Hello": "world"}

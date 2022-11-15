from typing import Callable
from fastapi import Request

async def request_adapter(request: Request, callback: Callable):
    """FastAPI Adapter"""

    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = {
        "query_params": request.query_params,
        "body": body
    }

    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('An error has occured')

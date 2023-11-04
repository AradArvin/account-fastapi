import httpx
from core import settings



async def httpx_response(authorization_endpoint: str, data: dict = None):
    print(data)
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.AUTHORIZATION_ADDRESS}/{authorization_endpoint}", json=data)

    return response.json()
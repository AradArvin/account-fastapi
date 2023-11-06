import httpx
from core import settings



async def httpx_response(authorization_endpoint: str, data: dict = None):

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.AUTHORIZATION_ADDRESS}/{authorization_endpoint}", json=data)

    return response.json()


async def httpx_response_otp(email_endpoint: str, data: dict = None):

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.EMAIL_ADDRESS}/{email_endpoint}", json=data)

    return response.json()
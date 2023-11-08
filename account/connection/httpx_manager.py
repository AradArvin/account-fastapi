import httpx
from core import settings



async def httpx_response(authorization_endpoint: str, data: dict):

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.AUTHORIZATION_ADDRESS}/{authorization_endpoint}", json=data)

    return response.json()



async def httpx_response_with_header(authorization_endpoint: str, auth_token: str = None):

    headers = {"Authorization": auth_token}
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.post(f"{settings.AUTHORIZATION_ADDRESS}/{authorization_endpoint}", json=None)

    return response.json()



async def httpx_response_with_header_and_data(authorization_endpoint: str, data: dict, auth_token: str = None):

    headers = {"Authorization": auth_token}
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.put(f"{settings.AUTHORIZATION_ADDRESS}/{authorization_endpoint}", json=data)

    return response.json()




async def httpx_response_otp(email_endpoint: str, data: dict):

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.EMAIL_ADDRESS}/{email_endpoint}", json=data)

    return response.json()
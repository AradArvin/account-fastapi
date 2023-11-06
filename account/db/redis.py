from redis import asyncio as aioredis

from core import settings


HOST_ADDRESS: str = settings.REDIS_HOST_ADDRESS 

redis = aioredis.from_url(HOST_ADDRESS, decode_responses=True)


async def check_otp(otp: str):

    all_keys = await redis.keys("*")

    for key in all_keys:
        if await redis.get(key) == otp:
            return key.split("_")[1]
    
    return None
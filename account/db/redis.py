from redis import asyncio as aioredis

from core import settings


HOST_ADDRESS: str = settings.REDIS_HOST_ADDRESS 

redis = aioredis.from_url(HOST_ADDRESS, decode_responses=True)



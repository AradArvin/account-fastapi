import jwt

from core import settings




async def token_decode(token: str):
    """Dencode tokens based on HS256 algorithm"""

    payload = jwt.decode(jwt=token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    return payload
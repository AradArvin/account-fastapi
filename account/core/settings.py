from decouple import config

# Main app settings


JWT_SECRET = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")


AUTHORIZATION_ADDRESS = "http://127.0.0.1:8001/authorization"

EMAIL_ADDRESS = "http://127.0.0.1:8002/email"

MONGODB_HOST_ADDRESS = "mongodb://localhost:27017/"

REDIS_HOST_ADDRESS = "redis://127.0.0.1:6379/1"


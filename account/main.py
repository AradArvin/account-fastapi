from fastapi import FastAPI

from api.api_v1.api import account_router, data_router


app = FastAPI()


app.include_router(account_router, tags=["accounts"], prefix="/account")
app.include_router(data_router, tags=["data"], prefix="/data")
from db.db import get_interaction_collection
from exception.exception import *
from connection.httpx_manager import httpx_response_with_header


class InteractionsService:

    def __init__(self, collection_name) -> None:
        self.collection = get_interaction_collection(collection_name)


    async def save_interaction_data(self, request, data):

        bearer = request.headers.get("Authorization")
        response = await httpx_response_with_header("api/v1/check-login", bearer)

        if response.get("status", None) == "logged_in":
            save = await self.collection.save_data_to_db_collection(data)
            return save
        else:
            raise UserNotLoggedInError
        

    async def get_interaction_data_list(self, request):

        bearer = request.headers.get("Authorization")
        response = await httpx_response_with_header("api/v1/check-login", bearer)

        if response.get("status", None) == "logged_in":
            data_list = await self.collection.get_data_from_db_collection()
            return data_list
        else:
            raise UserNotLoggedInError
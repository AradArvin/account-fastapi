from db.db import get_interaction_collection
from exception.exception import *
from connection.httpx_manager import httpx_response_with_header
from jwt_auth.utils import token_decode

# A service to perform user interactions
class InteractionsService:

    def __init__(self) -> None:
        pass


    async def save_interaction_data(self, request, data, collection_name):
        """
        Saves the interaction data for logged in user.
        """
        bearer = request.headers.get("Authorization")
        response = await httpx_response_with_header("api/v1/check-login", bearer)

        token_payload = token_decode(bearer.split(" ")[1])
        data["user_id"] = token_payload["user_id"]

        collection = get_interaction_collection(collection_name)

        if response.get("status", None) == "logged_in":
            save = await collection.save_data_to_db_collection(data)
            return save
        else:
            raise UserNotLoggedInError
        

    async def get_interaction_data_list(self, request, collection_name):
        """
        Returns the interaction data for logged in user.
        """
        bearer = request.headers.get("Authorization")
        response = await httpx_response_with_header("api/v1/check-login", bearer)

        token_payload = token_decode(bearer.split(" ")[1])
        user_id = token_payload["user_id"]

        collection = get_interaction_collection(collection_name)

        if response.get("status", None) == "logged_in":
            data_list = await collection.get_data_by_query("user_id", user_id)
            return data_list
        else:
            raise UserNotLoggedInError
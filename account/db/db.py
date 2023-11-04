from .mongodb import MongoDBConnectionManager

user_collection = MongoDBConnectionManager(database="users", collection="user_data")


def get_collection():
    return user_collection


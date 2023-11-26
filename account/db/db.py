from .mongodb import MongoDBConnectionManager

# MongoDB collections

user_collection = MongoDBConnectionManager(database="users", collection="user_data")

like_collection = MongoDBConnectionManager(database="interaction", collection="like")
comment_collection = MongoDBConnectionManager(database="interaction", collection="comment")
bookmark_collection = MongoDBConnectionManager(database="interaction", collection="bookmark")
subscribe_collection = MongoDBConnectionManager(database="interaction", collection="subscribe")


def get_collection():
    return user_collection


def get_interaction_collection(collection_name: str):
    """
    Return a collection based on the argument.
    """
    if collection_name == "like":
        return like_collection
    elif collection_name == "comment":
        return comment_collection
    elif collection_name == "bookmark":
        return bookmark_collection
    elif collection_name == "subscribe":
        return subscribe_collection
    else:
        return None
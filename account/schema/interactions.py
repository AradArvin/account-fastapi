from pydantic import Field, BaseModel


class Like(BaseModel):
    _id: str
    episode_id: str = Field()



class LikeResponse(BaseModel):
    episode_id: str
    user_id: str


class Comment(BaseModel):
    _id: str
    episode_id: str = Field()
    content: str = Field()


class CommentResponse(BaseModel):
    episode_id: str
    user_id: str
    content: str



class Bookmark(BaseModel):
    _id: str
    episode_id: str = Field()
    bookmark_list_name: str | None=None


class BookmarkResponse(BaseModel):

    episode_id: str
    user_id: str
    bookmark_list_name: str | None=None



class Subscribe(BaseModel):
    _id: str
    rss_id: str = Field()



class SubscribeResponse(BaseModel):
    rss_id: str
    user_id: str
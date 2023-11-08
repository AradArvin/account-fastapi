from pydantic import Field, BaseModel


class Like(BaseModel):
    _id: str
    episode_id: str = Field()
    user_id: str = Field()


class Comment(BaseModel):
    _id: str
    episode_id: str = Field()
    user_id: str = Field()
    content: str = Field()


class Bookmark(BaseModel):
    _id: str
    episode_id: str = Field()
    user_id: str = Field()
    bookmark_list_name: str | None=None


class Subscribe(BaseModel):
    _id: str
    rss_id: str = Field()
    user_id: str = Field()
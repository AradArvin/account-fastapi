from pydantic import Field, BaseModel


class Like(BaseModel):
    _id: str
    episode_id: str = Field()
    user_id: str = Field()



from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    theme: str
    description: str

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    ...


class PostResponse(PostBase):
    ...

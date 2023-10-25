from pydantic import BaseModel, ConfigDict


class BaseGenre(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class CreateGenre(BaseGenre):
    pass


class ViewGenre(BaseGenre):
    id: int



from pydantic import BaseModel, ConfigDict


class BaseAuthor(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class CreateAuthor(BaseAuthor):
    pass


class ViewAuthor(BaseAuthor):
    id: int

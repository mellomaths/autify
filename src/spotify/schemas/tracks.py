from pydantic import BaseModel


class Track(BaseModel):
    id: str
    name: str
    artists: str
    uri: str

from pydantic import BaseModel

class SpotifyApiHeaders(BaseModel):
    Authorization: str
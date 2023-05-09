from typing import List, Optional
from pydantic import BaseModel

from src.spotify.schemas.tracks import Track


class Artist(BaseModel):
    id: str
    name: str
    uri: str
    tracks: Optional[List[Track]]

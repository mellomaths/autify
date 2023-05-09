from pydantic import BaseModel
from typing import List

from src.spotify.schemas.tracks import Track


class CreatePlaylist(BaseModel):
    name: str
    description: str
    collaborative: bool
    public: bool
    tracks: List[Track]


class Playlist(BaseModel):
    id: str
    uri: str
    link: str

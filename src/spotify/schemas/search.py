from typing import List, Any
from pydantic import BaseModel


class ResultObject(BaseModel):
    href: str
    limit: int
    next: str
    offset: int
    previous: str | None
    total: int
    items: List[Any]


class SearchResult(BaseModel):
    tracks: ResultObject | None
    artists: ResultObject | None
    albums: ResultObject | None
    playlists: ResultObject | None
    shows: ResultObject | None
    episodes: ResultObject | None
    audiobooks: ResultObject | None

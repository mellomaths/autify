from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def spotify_callback(code: str, state: str):
    return

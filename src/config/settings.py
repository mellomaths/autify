from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    
    spotify_redirect_uri: str
    spotify_client_id: str
    spotify_client_secret: str

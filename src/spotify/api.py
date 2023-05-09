import random
import spotipy

from typing import List
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from src.config.settings import Settings
from src.spotify.schemas.playlists import CreatePlaylist, Playlist
from src.spotify.schemas.search import SearchResult
from src.spotify.schemas.artists import Artist
from src.spotify.schemas.tracks import Track


class SpotifyApi():

    def __init__(self) -> None:
        self.base_url = "https://api.spotify.com/v1"
        self.settings = Settings()
        self.credentials = SpotifyClientCredentials(client_id=self.settings.spotify_client_id, client_secret=self.settings.spotify_client_secret)
        self.oauth = SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=self.settings.spotify_redirect_uri,
            client_id=self.settings.spotify_client_id,
            client_secret=self.settings.spotify_client_secret,
        )
        self.client = spotipy.Spotify(auth_manager=self.oauth)


    def create_playlist(self, user_id: str, playlist: CreatePlaylist) -> Playlist:
        result = self.client.user_playlist_create(user=user_id, name=playlist.name, public=playlist.public, collaborative=playlist.collaborative, description=playlist.description)
        print(playlist)
        playlist = Playlist(id=result["id"], uri=result["uri"], link=result["external_urls"]["spotify"])
        return playlist

    def get_artist(self, artist_name: str) -> Artist:
        result: dict = self.client.search(q=artist_name, type="artist")
        result = SearchResult(**result)
        if result.artists is None:
            return None

        artist = result.artists.items[0]
        return Artist(id=artist["id"], name=artist["name"], uri=artist["uri"])

    def get_tracks_from_artist(self, artist_id: str) -> List[Track]:
        result = self.client.artist_top_tracks(artist_id=artist_id)
        track = None
        track_list: List[Track] = []
        while len(track_list) != 3:
            track = random.choice(result['tracks'])
            artists_names_list = [artist["name"] for artist in track["artists"]]
            artists = ", ".join(artists_names_list)
            insert_track = True
            for track_inserted in track_list:
                insert_track = track["name"] not in track_inserted.name and track_inserted.name not in track["name"]
                if not insert_track:
                    break

            if insert_track:
                track_list.append(Track(id=track["id"], name=track["name"], artists=artists,uri=track["uri"]))

        return track_list

    def get_tracks_related_to_artist(self, artist_id: str) -> List[Artist]:
        result = self.client.artist_related_artists(artist_id=artist_id)
        # print(result)
        artist_list: List[Artist] = []
        while len(artist_list) != 3:
            artist = random.choice(result["artists"])
            add_artist = True
            for artist_added in artist_list:
                add_artist = artist["name"] == artist_added.name
                if not add_artist:
                    break

            if add_artist:
                artist_list.append(Artist(id=artist["id"], name=artist["name"], uri=artist["uri"]))
        

        for artist in artist_list:
            artist.tracks = self.get_tracks_from_artist(artist_id=artist.id)
            
        return artist_list

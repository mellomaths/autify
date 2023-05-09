from src.spotify.api import SpotifyApi
from src.spotify.schemas.playlists import CreatePlaylist, Playlist


def run():
    spotify = SpotifyApi()
    artist = spotify.get_artist("A$AP Rocky")
    print(artist.id, artist.name, artist.uri)
    tracks = spotify.get_tracks_from_artist(artist_id=artist.id)
    # print(tracks)
    for track in tracks:
        print(track.id, track.name)
    artists = spotify.get_tracks_related_to_artist(artist_id=artist.id)
    print()
    for artist in artists:
        print(artist.id, artist.name)
        for track in artist.tracks:
            print(track.id, track.name)
        print()

    playlist = CreatePlaylist(name="08/05/2023", description="Playlist diária", collaborative=False, public=False, tracks=tracks)
    spotify.create_playlist(user_id="12146450182", playlist=playlist)

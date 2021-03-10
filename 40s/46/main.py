import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR SECRET CLIENT"
REDIRECT_URI = "http://example.com"

# date for search
date = input(
    "Which year do you want to travel to?  Type the data in the format YYYY-MM-DD\n")

# request billboard data
billboard_response = requests.get(URL)
billboard_data = billboard_response.text

# parse through data
soup = BeautifulSoup(billboard_data, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song")
song_titles = [song.getText() for song in songs]
song_uris = []
year = date[0:4]

# authenticate to spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# search for the song in spotify and add to the song uri list.
# if the song is not on spotify, except the error and move onto the next one
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not on Spotify.")

# create private playlist and add songs to it
new_playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public="False")
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)

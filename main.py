from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

#Autentificare pe spotify

def autentificare_spotify():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID_CLIENT,
                                                        client_secret=SECRET_CLINET,
                                                        redirect_uri=URI_REDIRECT,
                                                        scope=SCOPE,
                                                        show_dialog=True,
                                                        cache_path="token.txt"))
        print("Autentificarea s-a facut cu succes")
        return sp
    except Exception as e:
        print(f"Eroare la autentificare {e}")
        return None


def creeaza_playlist(sp, nume_playlist, descriere="Playlist creat cu Spotipy"):
    try:
        user_id = sp.current_user()["id"]
        playlist = sp.user_playlist_create(user=user_id,
                                        name=nume_playlist,
                                        description=descriere,
                                        public=True)
        print(f"Playlist ul a fost creat cu succes")
        return playlist["id"]
    except Exception as e:
        print(f"Eroare la crearea playlist-ului: {e}")
        return None
    
def cauta_piesa(sp,limit=1):
    with open(file="/Users/01mih/OneDrive/Desktop/PYTHON/Spotify/lista_piese.txt", mode="r", encoding="utf-8") as file:
        piese = file.readlines()
    track_ids = []

    for piesa in piese:
        piesa = piesa.strip() # Eliminarea spatiilor inutile
        try:
            rezultat = sp.search(q=piesa,type="track",limit=limit)
            track_id = rezultat["tracks"]["items"][0]["id"] # ID ul cu care cautam piesa pe Spotify
            track_ids.append(track_id)
        except IndexError:
            print("Nu s-a gasit o piesa")
        except Exception as e:
            print(f"Eroare la catarea piesei {e}")
    # with open(file="/Users/01mih/OneDrive/Desktop/PYTHON/Spotify/track_ids.txt", mode="w", encoding="utf-8") as file:
    #     for track_id in track_ids:
    #         file.write(f"{track_id}\n")
    # print("ID urile pieselor au fost salvate in track_ids.txt")
    return track_ids

def adauga_piese(sp,track_ids,playlist_id):
    try:
        sp.playlist_add_items(playlist_id=playlist_id,
                              items=track_ids,
                              position=None)
        print("Au fost adaugate piesele")
        return True
    except Exception as e:
        print(f"Nu au fost adaugate piesele in {e}")
        return False


#Main ul
date = input("Enter a track date in YYYY-MM-DD format:")
name_playlist = input("Enter a playlist name:")
url = f"https://www.billboard.com/charts/hot-100/{date}"
ID_CLIENT = "9a9fcf2f034f4adcba05154804c01c12"
SECRET_CLINET = "f323deab3f4248f1868a1644bcbc09b6"
URI_REDIRECT = "http://example.com"
SCOPE = "playlist-modify-public playlist-modify-private user-library-read"
CODE = "31q3urkvzrgg6l7e7i6qv3k7r4ky"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url=url, headers=headers)
html_data = response.text
soup = BeautifulSoup(html_data,"html.parser")

song_names_spans = soup.select("li ul li h3")
with open(file="/Users/01mih/OneDrive/Desktop/PYTHON/Spotify/lista_piese.txt", mode="w", encoding="utf-8") as file:
    for i in song_names_spans:
        songs = i.get_text().strip()
        file.write(f"{songs}\n")


sp = autentificare_spotify()
if not sp:
    print("Nu s-a putut realiza autentificarea la spotify")
playlist_id = creeaza_playlist(sp=sp,nume_playlist=name_playlist,descriere="Creat cu spotipy")
final_track_list = cauta_piesa(sp=sp)
adauga_piese(sp=sp,track_ids=final_track_list,playlist_id=playlist_id)



       
    
    





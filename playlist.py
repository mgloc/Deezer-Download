import deezer
import time
import requests
import json
import time

#Var
client = deezer.Client()
from_date = round(time.time() - 30*24*60*60)

#Func
def get_user(username) :
    return client.get_user(username)

def get_track(trackid) :
    return client.get_track(trackid)

def get_tracks_id_and_time_add_from_playlist(playlist,limit) :
    url_track_list = playlist.as_dict()['tracklist'] +f"?limit={limit}"
    track_list = json.loads(requests.get(url_track_list).text)['data']
    
    return [ [i['id'],i['time_add']] for i in track_list ]

#Récuperation des utilisateurs
def get_available_user_from_txt() :
    user_list = []
    with open("user_deezer.txt", "r") as f :
        for x in f :
            user_list.append((x[:10],x[11:].replace("\n","")))
    return(user_list)

#Listage de tout les titres de toute les playlist de tout les utilisateurs sans occ
def get_all_tracks_id(from_date=from_date) :
    major_track_list = []

    temp = get_available_user_from_txt()
    users_list = [get_user(i[0]) for i in temp]
    for user in users_list :
        user_playlists = user.get_playlists()

        for playlist in user_playlists :
            tracks_list = get_tracks_id_and_time_add_from_playlist(playlist,limit=1000)
            for track in tracks_list :
                if not(track[0] in major_track_list) and track[1] >= from_date :
                    major_track_list.append(track[0])

    return major_track_list

def get_all_tracks(from_date=from_date):
    liste = get_all_tracks_id()
    temp = []
    for i in liste :
        try :
            e = get_track(i)
            temp.append(e)
        except ValueError :
            pass
    return temp

def get_artist(track):
    string = (track.get_artist()).__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

def get_title(track):
    string = track.__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])
#################################################################################################

class getter :

    def __init__(self) :
        self.actualise_playlist()

    def actualise_date(self):
        self.from_date = round(time.time() - 30*24*60*60)
    
    def actualise_playlist(self):
        self.actualise_date()
        self.playlist = get_all_tracks(from_date=self.from_date)

    def get_track(self):
        if len(self.playlist) == 0 :
            self.actualise_playlist()
            get_track()
        else :
            track = self.playlist.pop()
            return [get_title(track),get_artist(track)]
    
        


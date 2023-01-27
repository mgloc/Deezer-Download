# --------------------- IMPORTS ---------------------
import deezer
import time
import requests
import json
import time

# Client
client = deezer.Client()
default_limit = 1000
threshold = 42
from_date = round(time.time() - 30*24*60*60)
sample_username = "2278880688"

# --------------------- GETTERS ---------------------
# User ID
def getUsersFromFile(filename="user_deezer.txt") :
    user_list = []
    with open(filename, "r") as f :
        for x in f :
            user_list.append((x[:10],x[11:].replace("\n","")))
    return(user_list)

# User

def getUser(username) :
    return client.get_user(username)

# Tracks

def TracksFromPlaylist(playlist,limit=default_limit) :
    return playlist.get_tracks(limit=limit)


def getTrack(trackid) :
    return client.get_track(trackid)

# Playlist ID
def getPlaylist(playlist_id:int):
    return client.get_playlist(playlist_id)

def getPlaylists(user) :
    return user.get_playlists()


def getLovedTracks(user) :
    for playlist in getPlaylists(user) :
        if playlist.as_dict()['title'] == "Loved Tracks" :
            return playlist
    return None

# Artiste

def getArtiste(track):
    string = (track.artist).__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

# Title
def getTitle(track):
    string = track.__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

# Song
def getSongString(track):
    return(getTitle(track) + " - " + getArtiste(track))

def getAllSongsFromPlaylist(playlist,limit=default_limit):
    tracks = TracksFromPlaylist(playlist,limit)
    songs = []
    counter = 0
    for track in tracks :
        if counter > threshold :
            counter = 0
            print("Quota exceeded, sleeping for 5 seconds")
            time.sleep(5)
        songs.append(getSongString(track))
        counter+=1
    return songs 

def getAllSongsFromLovedTracks(user,limit=default_limit):
    return getAllSongsFromPlaylist(getLovedTracks(user),limit=limit)



if "__main__" == __name__ :
    sample_user = getUser(sample_username)
    print(getPlaylists(sample_user))

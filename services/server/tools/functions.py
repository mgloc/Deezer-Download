# ------------------------------ IMPORTS ------------------------------
import tools.fetch.fetch_deezer as fd
import tools.fetch.fetch_youtube as fy


def getUserById(user_id):
    try :
        user = fd.getUser(user_id)
        return {"id":user.id,"name":user.name}
    except :
        return {"error":"user not found"}

def getPlaylistById(playlist_id):
    try:
        playlist = fd.getPlaylist(playlist_id)
        return {"id":playlist.id,"title":playlist.title}
    except :
        return {"error":"playlist not found"}

def getUserPlaylists(user_id):
    try :
        user = fd.getUser(user_id)
    except :
        return {"error":"user not found"}
    
    playlists:list = fd.getPlaylists(user)
    return list(map(lambda pl : {"id":pl.id,"title":pl.title} ,playlists))

def downloadDeezerPlaylistByID(playlist_id,path="."):
    try :
        playlist = fd.getPlaylist(playlist_id)
    except :
        return {"error":"playlist not found"}

    songs = fd.getAllSongsFromPlaylist(playlist)
    for song in songs:
        print("Downloading " + song)
        fy.getAndDownloadYoutubeMusic(song, path=path, filename=song)
    print("Done")

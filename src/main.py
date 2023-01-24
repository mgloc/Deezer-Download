# ------------------------------ IMPORTS ------------------------------
import fetch.fetch_deezer as fd
import fetch.fetch_youtube as fy

# Functions
def downloadDeezerPlaylist(username, playlist_name, path="."):
    # Deezer part
    user = fd.getUser(username)
    playlists = fd.getPlaylists(user)
    playlist = list(filter(lambda x: playlist_name in str(x.__repr__()), playlists))
    if len(playlist) == 0:
        print("Playlist not found")
        return
    elif len(playlist) > 1:
        print("Playlist name not unique, choosing first one")
    playlist = playlist[0]
    songs = fd.getAllSongsFromPlaylist(playlist)
    
    # Youtube part
    for song in songs:
        print("Downloading " + song)
        fy.getAndDownloadYoutubeMusic(song, path=path, filename=song)
    
    print("Done")


def downloadDeezerLovedTracks(username, path="."):
    return downloadDeezerPlaylist(username, "Loved Tracks", path)

if __name__ == "__main__":
    downloadDeezerPlaylist(username=fd.sample_username, playlist_name="deep & lofi")
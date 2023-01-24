from pytube import YouTube,Search
from youtube_search import YoutubeSearch
import os

def downloadYoutubeMusic(url, path=".",filename="nofilename"):
    """Download the youtube music url in the path with the filename"""
    # Format file name
    temp = filename
    filename = ''.join(e for e in temp if e.isalnum() or e == '_')

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    download  = video.download(output_path=path)
    new_file = filename + '.mp3'
    os.rename(download, new_file)
    print("Downloaded " + filename)

def getFirstYoutubeResult(title):
    """Return the first youtube url found for the filename"""
    results = YoutubeSearch(title, max_results=1).to_dict()
    try :
        print("Music found")
        url = "https://www.youtube.com" + results.pop()["url_suffix"]
    except :
        url = None
        print("No music found for " + title)
    return url

def getFirstYoutubeResultOnlyMusic(title):
    """Return the first youtube url found for the filename, with only music by adding the keyword lyrics"""
    return getFirstYoutubeResult(title + " lyrics")

def getAndDownloadYoutubeMusic(title, path=".",filename="nofilename"):
    """Get the first youtube url found for the filename and download it in the path with the filename"""
    url = getFirstYoutubeResultOnlyMusic(title)
    if url != None :
        downloadYoutubeMusic(url, path, filename)

if __name__ == "__main__":
    getAndDownloadYoutubeMusic("The Weeknd Blinding Lights", path=".",filename="The Weeknd Blinding Lights")
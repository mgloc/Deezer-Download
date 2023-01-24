from pytube import YouTube,Search
import os

def downloadYoutubeMusic(url, path=".",filename="nofilename"):
    """Download the youtube music url in the path with the filename"""
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    download  = video.download(output_path=path)
    new_file = filename + '.mp3'
    os.rename(download, new_file)

def getFirstYoutubeResult(title):
    """Return the first youtube url found for the filename"""
    search = Search(title)
    try :
        url = search.results[0].url
    except :
        url = None
    return url

def getFirstYoutubeResultOnlyMusic(title):
    """Return the first youtube url found for the filename, with only music by adding the keyword lyrics"""
    return getFirstYoutubeResult(title + " lyrics")

def getAndDownloadYoutubeMusic(title, path=".",filename="nofilename"):
    """Get the first youtube url found for the filename and download it in the path with the filename"""
    url = getFirstYoutubeResultOnlyMusic(title)
    if url != None :
        downloadYoutubeMusic(url, path, filename)

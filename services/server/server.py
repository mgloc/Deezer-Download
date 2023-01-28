from flask import Flask, send_from_directory, jsonify
from tools import functions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def base():
    return send_from_directory("../client/public", "index.html")

# TEST API

@app.route("/testapi")
def test_api_root():
    return "testapi_root"

@app.route("/testapi/user/<user_id>")
def test_get_user(user_id):
    return {"id":11234,"name":"dummyUser"}

@app.route("/testapi/user/<user_id>/playlists")
def test_get_user_playlists(user_id):
    return [{"id":10192,"title":"Playlist 1"},{"id":10192,"title":"Playlist 2"}]

@app.route("/testapi/playlist/<playlist_id>")
def test_get_playlist(playlist_id):
    return {"id":10192,"title":"Playlist 1"}

@app.route("/testapi/playlist/<playlist_id>/tracks")
def test_get_playlist_tracks(playlist_id):
    return [{"id":10192,"title":"Track 1"},{"id":10192,"title":"Track 2"},{"id":10192,"title":"Track 3"}]

@app.route("/testapi/playlist/<playlist_id>/download")
def test_download_playlist(playlist_id):
    return {"status":"downloaded"}

# API

@app.route("/api")
def api_root():
    return "api_root"

@app.route("/api/user/<user_id>")
def get_user(user_id):
    res = functions.getUserById(user_id)
    return res

@app.route("/api/user/<user_id>/playlists")
def get_user_playlists(user_id):
    return functions.getUserPlaylists(user_id)

@app.route("/api/playlist/<playlist_id>")
def get_playlist(playlist_id):
    return functions.getPlaylistById(playlist_id)

@app.route("/api/playlist/<playlist_id>/download")
def download_playlist(playlist_id):
    functions.downloadDeezerPlaylistByID(playlist_id)
    return {"status":"downloaded"}

@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
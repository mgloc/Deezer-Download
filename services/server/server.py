from flask import Flask, send_from_directory
from tools import functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def base():
    return send_from_directory("../client/public", "index.html")

@app.route("/api")
def api_root():
    return "api_root"

@app.route("/api/user")
def get_user():
    return ""

@app.route("/api/user/<user_id>")
def get_user_playlists(user_id):
    return user_id

@app.route("/api/user/<user_id>")

@app.route("/api/playlists/<playlist_id>")
def get_playlist_tracks(playlist_id):
    return playlist_id

@app.route("/api/download/<playlist_id>")
def download_playlist(playlist_id):
    return playlist_id

@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
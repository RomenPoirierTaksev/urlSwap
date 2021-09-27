from flask import Flask, render_template, request, jsonify
from urlSwapSP import getSpotifyName,getSpotifyURL
from urlSwapAM import getAppleMusicName,getAppleMusicURL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/hello", methods=['GET', 'POST'])
def get_js_data():
    if request.method == "GET":
        return jsonify('YOo')

    if request.method == 'POST':
        url = str(request.get_json())  # parse as JSON
        if("https://open.spotify.com/" in url or "https://music.apple.com/" in url):
            link_type = "spotify" if "https://open.spotify.com/" in url else "apple"
            if link_type == "spotify":
                return getAppleMusicURL(getSpotifyName(url))
            else:
                return getSpotifyURL(getAppleMusicName(url))
        else:
            return "Invalid URL" , 400


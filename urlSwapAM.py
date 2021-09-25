import pip._vendor.requests as requests

def getAppleMusicURL(name):

    name_list = name.split("&")

    r = requests.get("https://itunes.apple.com/search?term={name_list[0]}&type=music".format(name_list=name_list))

    r = r.json()

    for track in r['results']:
        try:
            track_name = track['trackName']
            track_artist = track['artistName']
            if (track_name.title().find(name_list[0].title()) != -1) and (track_artist.title().find(name_list[1].title()) != -1):
                return track['trackViewUrl']
        except:
            pass


def getAppleMusicName(url):
    x = url.find("i=")
    track_id = url[x+2:x+12]

    r = requests.get("https://itunes.apple.com/lookup?id={track_id}".format(track_id=track_id))

    r = r.json()['results'][0]

    try:
        an = r['artistName'].split('&')
        return '&'.join([r['trackName'], an[0]])
    except:
        return '&'.join([r['trackName'], r['artistName']])

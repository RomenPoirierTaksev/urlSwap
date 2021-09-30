import pip._vendor.requests as requests

def getAppleMusicURL(name):

    name_list = name.split("%")
    name_list[0] = name_list[0][0:name_list[0].find("(")]
    name_list[0] = name_list[0][0:name_list[0].find("-")]
    r = requests.get("https://itunes.apple.com/search?term={name_list[0]}&type=music&entity=song&limit=200".format(name_list=name_list))
    r = r.json()

    #print(r)
    count = 1
    for track in r['results']:
        try:
            track_name = track['trackName']
            track_artist = track['artistName']
            print("----------{count}-----------".format(count=count))
            print(track_name, track_artist)
            print(name_list[0],name_list[1])
            print("----------------------")
            count += 1
            if (track_name.lower().find(name_list[0].lower()) != -1) and (track_artist.lower().find(name_list[1].lower()) != -1):
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
        return '%'.join([r['trackName'], an[0]])
    except:
        return '%'.join([r['trackName'], r['artistName']])

import pip._vendor.requests as requests

CLIENT_ID = ""
CLIENT_SECRET = ""

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

#print(access_token)

headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

BASE_URL = 'https://api.spotify.com/v1/'



def getSpotifyURL(name):

    name_list = name.split("%")
    name_list[0] = name_list[0][0:name_list[0].find("(")] if name_list[0].find("(") != -1 else name_list[0]
    name_list[0] = name_list[0][0:name_list[0].find("-")] if name_list[0].find("-") != -1 else name_list[0]
    name_list[0] = name_list[0].strip()
    name_list[1] = name_list[1].strip()
    print(name_list)
    r = requests.get(BASE_URL + 'search?' + "q={name}&type=track&limit=50".format(name=name_list[0]), headers=headers)

    r = r.json()

    for track in r['tracks']['items']:
        try:
            track_name = track['name']
            track_artist = track['artists'][0]['name']
            print(track_name, name_list[0])
            print(track_artist, name_list[1])
            if (track_name.lower().find(name_list[0].lower()) != -1) and (track_artist.lower().find(name_list[1].lower()) != -1):
                return track['external_urls']['spotify']
        except:
            pass


def getSpotifyName(url):
    
    track_id = url[31:]
    print(track_id)
    r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)

    r = r.json()

    print('%'.join([r['name'], r['artists'][0]['name']]))
    return '%'.join([r['name'], r['artists'][0]['name']])





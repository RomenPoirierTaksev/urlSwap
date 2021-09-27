from urlSwapSP import getSpotifyName,getSpotifyURL
from urlSwapAM import getAppleMusicName,getAppleMusicURL


#To get an Apple Music URL from a Spotify URL

#print(getAppleMusicURL(getSpotifyName("https://open.spotify.com/track/0k1WUmIRnG3xU6fvvDVfRG")))

#To get a Spotify URL from an Apple Music URL

print(getSpotifyURL(getAppleMusicName("https://music.apple.com/us/album/way-2-sexy-feat-future-young-thug/1584281467?i=1584281770&uo=4")))
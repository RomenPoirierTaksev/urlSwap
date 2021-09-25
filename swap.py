from urlSwapSP import getSpotifyName,getSpotifyURL
from urlSwapAM import getAppleMusicName,getAppleMusicURL


#To get an Apple Music URL from a Spotify URL

print(getAppleMusicURL(getSpotifyName("https://open.spotify.com/track/7KA4W4McWYRpgf0fWsJZWB")))

#To get a Spotify URL from an Apple Music URL

print(getSpotifyURL(getAppleMusicName("https://music.apple.com/ca/album/thats-what-i-want/1582660720?i=1582660725")))
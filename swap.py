from urlSwapSP import getSpotifyName,getSpotifyURL
from urlSwapAM import getAppleMusicName,getAppleMusicURL


#To get an Apple Music URL from a Spotify URL

print(getAppleMusicURL(getSpotifyName("https://open.spotify.com/track/6Qj1WXW41Mn3Fh9V2sHphM")))

#To get a Spotify URL from an Apple Music URL

#print(getSpotifyURL(getAppleMusicName("https://music.apple.com/us/album/moves-like-jagger-feat-christina-aguilera/1440858689?i=1440859510&uo=4")))
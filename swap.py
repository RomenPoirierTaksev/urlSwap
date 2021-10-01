from urlSwapSP import getSpotifyName,getSpotifyURL
from urlSwapAM import getAppleMusicName,getAppleMusicURL


#To get an Apple Music URL from a Spotify URL

#print(getAppleMusicURL(getSpotifyName("https://open.spotify.com/track/4wvnXoQqjIOoEis5eyTbCl")))

#To get a Spotify URL from an Apple Music URL

print(getSpotifyURL(getAppleMusicName("https://music.apple.com/us/album/money-trees-feat-jay-rock/1440818890?i=1440818969&uo=4")))

import lastfm

API_KEY = "" # Insert your last.fm api key here
USER_NAME = "" # Insert your last.fm username here

lastFMClient = lastfm.Client(API_KEY)

class Scrobbler:

    # Main scrobbling func, using lastfm-py
    async def __scrobble(self):
        trackReqeust = await lastFMClient.user_get_recent_tracks(USER_NAME, limit=1)
        lastTrack = trackReqeust['recenttracks']['track'][0]

        return lastTrack
    
    # Returns the title of the track in the format "title - artist"
    async def getCompleteName(self):
        result = await self.__scrobble()
        return result['name'] + " - " + result['artist']['name']
    
    # Returns a list ["songTitle", "authorName"]
    async def getSplitTitle(self):
        splitName = await self.getCompleteName()
        return splitName.split("-")
    
    # Returns if the last track on the list is now playing
    async def nowPlaying(self):
        try:
            check = await self.__scrobble()
            if check['@attr']['nowplaying'] == "true":
                return True
            else: return False
        except:
            return False
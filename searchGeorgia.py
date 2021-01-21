from twitter import * 

OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


# can use scraper to find locations that need to be found, found in locationmetadata file 
# however, best use would be to write to this file with locations you want to search

def getLocations() : 
    f = open("LocationMetaData.txt", "r")
    locations = f.read()
    locations = locations.split('\n')
    locations.pop()
    return locations


# can use a maps type API to find radius of a town/state/county with a radius we need to search
# we can use different sites like realclearpolitics or other news sites to find locations and 
# campaign news and/or hashtangs to follow, then use maps to find radius of search area
# right now its a simple manual input of atlanta geo location with an approximate radius of the state

def getLatLongRange() : 
    f = open("LatLongRange.txt", "r")
    ranges = f.read()
    ranges = ranges.split('\n')
    ranges.pop()
    return ranges

# initialize twiter object
def initization() : 
    return Twitter(auth=OAuth(OAUTH_TOKEN,OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#main function, obtain tweets and store them in a file
def obtainTweets() : 
    t = initization()
    searchCriteria = getLocations()
    geoLocations = getLatLongRange()
    for i in range(len(searchCriteria)) : 
        hashtag = searchCriteria[i] 
        geo = geoLocations[i]
        data = t.search.tweets(q=hashtag,geocode=geo)
        f = open(searchCriteria[i] + 'TweetData.txt', "w")
        for i in data['statuses'] :
            data = i['text'].encode('ascii', 'ignore')
            f.write(data)
        f.close()

obtainTweets()

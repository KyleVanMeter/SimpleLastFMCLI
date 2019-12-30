#!/usr/bin/env python3
import requests
import json

class LastAPI:
    def __init__(self, APIKey):
        self.key = APIKey

    def getTrackInfo(self, user):
        self.userName = user

        return self.makeRequest(user)

    def makeRequest(self, user):
        self.url = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&limit=1&user=" + self.userName + "&api_key=" + self.key + "&format=json"
        #print("Requesting url: ", self.url)

        self.data = requests.get(self.url)
        self.json = self.data.json()

        return self.json

def main():
    with open("/home/kyle/code/lastfm/lastfm") as f:
        content = f.read().splitlines()

    data = []
    for x in content:
        data.append(x.split()[2])

    #print(data)

    appName  = data[0]
    key      = data[1]
    secret   = data[2]
    userName = data[3]

    x = LastAPI(key)

    result = x.getTrackInfo(userName)

    #print(json.dumps(result))

    if('@attr' in result['recenttracks']['track'][0]):
        print(result['recenttracks']['track'][0]['artist']['#text'] + ' - ' + result['recenttracks']['track'][0]['name'])
    else:
        print('???')


main()


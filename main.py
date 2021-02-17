
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import time

#PyLyrics-1.1.0
from PyLyrics import *        

import json


import requests
import re

client_id = #
client_secret = #

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

album = 'saturation'
artist = 'drake'
song = 'heartbeat'



'''
times = 50
total = 0
total1 = 0
for i in range(times):
    start = time.time()
    lyrics = data_scrape.scrape_lyrics(song, artist)
    end = time.time()
    lyrics1 = PyLyrics.getLyrics(artist, song)
    end1 = time.time()
    total = total + end - start
    total1 = total1 + end1 - end
total = total / times
total1 = total1 / times
'''

times = 50
new = 0
for i in range(times):
    a = time.time()
    try:
        lyrics1 = PyLyrics.getLyrics(artist, song)
    except:
        pass
    b = time.time()
    new = new + b - a
new = new / times












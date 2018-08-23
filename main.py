
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import time
        
album = 'saturation'
artist = 'brockhampton'
song = 'alaska'

'''
if title != '':
    song_list = data_scrape.search_album_id(title, artist)
else:
    song_list = data_scrape.search_song_id(title, artist)

#df = data_scrape.assemble_df(song_list, artist)

banger_or_nah = banger.test(title, artist, 1)
'''
#    analysis = sp.audio_analysis(id)
#    valence = valence_analysis(id)
#    mood = mood_analysis(lyrics, id)
    
#testdf = data_scrape.assemble_df(data_scrape.search_song_id(title, artist))
#testval = testdf.at(0,'energy')
#print(testval)
#data_scrape.print_df(data_scrape.assemble_df(data_scrape.search_song_id(title, artist)))


total = 0
for i in range(10):
    start = time.time()
    df = data_scrape.assemble_df(data_scrape.search_album_id(album, artist))
    end = time.time()
    total += end - start
total = total/10







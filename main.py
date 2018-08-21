
import banger
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


        
album = 'saturation'
artist = 'brockhampton'
playlist = ''

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
client_id = '91df6ca120d7407a877a64fabb100b49'
client_secret = '05a35b3ad63948c398d82dc8251d2bfb'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)






df = data_scrape.search_album_id(album, artist)
apply = df.apply
df['lyrics'] = apply(lambda row: data_scrape.scrape_lyrics(row['track'], row['artist']),1)
df['Lyrical Sentiment'] = apply(lambda row: data_scrape.sentiment_analysis(row['lyrics']) ,1)
df['Reading Level'] = apply(lambda row: data_scrape.reading_level(row['lyrics']) ,1)
df['Word Frequency'] = apply(lambda row: data_scrape.word_frequency(row['lyrics']) ,1)
for i, row in df.iterrows():
    features = sp.audio_features(row['id'])[0]
    df.append(features, ignore_index = True)












# -*- coding: utf-8 -*-
import pandas as pd
import requests
import re
import nltk
from textstat.textstat import textstat
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#nltk.download('vader_lexicon')
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import Counter
import banger
import timeit
import multiprocessing



client_id = '91df6ca120d7407a877a64fabb100b49'
client_secret = '05a35b3ad63948c398d82dc8251d2bfb'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



def scrape_lyrics(title, artist):
    ##Takes the Url and strips the html down to just the lyrics
    ##The Lyrics are placed into var clean
    title = title.replace(" ", "-").replace("/", "-").replace("&", "and")
    title = re.sub('[^0-9a-zA-Z-]+', '', title)
    title = re.sub('--*','-', title)
    artist = artist.replace(" ", "-").replace("/", "-").replace("&", "and")
    artist = re.sub('[^0-9a-zA-Z-]+', '', artist)
    artist = re.sub('--*','-', artist)
    source = requests.get('https://genius.com/'+artist+'-'+title+'-lyrics')
    if source.status_code == 404:
        return ' '
    return re.sub('<[^>]+>', '', source.text.split('<div class="lyrics">')[1].split('<!--/sse-->')[0]).strip()

def sentiment_analysis(lyrics):
    #in future get rid of brackets that have artist name
    return SentimentIntensityAnalyzer().polarity_scores(lyrics)['compound']
    

def valence_analysis(id):
    valence = sp.audio_features(id)[0]
    valence = valence['valence']
    return valence

def mood_analysis(lyrics, id):
    sentiment = sentiment_analysis(lyrics)
    sentiment = sentiment['compound']
    valence = valence_analysis(id)
    if sentiment < 0:
        if valence < .5:
            return "Angry"
        else:
            return "Hopeful"
    else:
        if valence < .5:
            return "Sad"
        else:
            return "Happy"

    

#This will need to run for each line separately, otherwise its useless
def scansion_scanner(lyrics):
    sc = textstat.syllable_count(lyrics)
    return sc

def word_frequency(lyrics):
    return Counter(lyrics.split()).most_common()
    
#decided which formula to use from documentation and this guide
#https://pypi.org/project/textstat/
#http://www.readabilityformulas.com/articles/how-do-i-decide-which-readability-formula-to-use.php
def reading_level(lyrics):
    r = textstat.flesch_kincaid_grade(lyrics)
    if r >= 90:
        return '5th Grade'
    elif r >=65:
        return 'Middle School'
    elif r >=50:
        return 'High School'
    elif r >= 30:
        return 'College'
    else:
        return 'College Graduate'
#100.00-90.00 	5th grade 	Very easy to read. Easily understood by an average 11-year-old student.
#90.0–80.0 	6th grade 	Easy to read. Conversational English for consumers.
#80.0–70.0 	7th grade 	Fairly easy to read.
#70.0–60.0 	8th & 9th grade 	Plain English. Easily understood by 13- to 15-year-old students.
#60.0–50.0 	10th to 12th grade 	Fairly difficult to read.
#50.0–30.0 	College 	Difficult to read.
#30.0–0.0 	College graduate 	Very difficult to read. Best understood by university graduates. 

def search_song_id_deprecated(title, artist):
    result = sp.search(q = title + ' ' + artist, limit = 1, type = 'track')
    result = result['tracks']
    result = result['items'][0]
    return result['id']

def search_song_id(title, artist):
    return sp.search(q = title + ' ' + artist, limit = 1, type = 'track')['tracks']['items'][0]['id']

def search_album_id(album, artist):  
    df = pd.DataFrame()
    tracks = sp.album_tracks(sp.search(q = album + ' ' + artist, limit = 1, type = 'album')['albums']['items'][0]['id'])['items']
    dat = df.at
    for i in range(len(tracks)):
        dat[i, 'track'] = re.sub("'","`", tracks[i]['name'])
        dat[i, 'artist'] = artist
        dat[i, 'id'] = tracks[i]['id']
    return df


def search_album_id_deprecated(album, artist):  
    df = pd.DataFrame()
    result = sp.search(q = album + ' ' + artist, limit = 1, type = 'album')
    result = result['albums']
    result = result['items'][0]
    tracks = sp.album_tracks(result['id'])
    tracks = tracks['items']
    for i in range(len(tracks)):
        df.at[i, 'track'] = re.sub("'","`", tracks[i]['name'])
        df.at[i, 'artist'] = artist
        df.at[i, 'id'] = tracks[i]['id']
    return df


def assemble_df(df):
    apply = df.apply
    df['lyrics'] = apply(lambda row: scrape_lyrics(row['track'], row['artist']),1)
    df['Lyrical Sentiment'] = apply(lambda row: sentiment_analysis(row['lyrics']) ,1)
    df['Reading Level'] = apply(lambda row: reading_level(row['lyrics']) ,1)
    df['Word Frequency'] = apply(lambda row: word_frequency(row['lyrics']) ,1)
    dat = df.at
    for i, row in df.iterrows():
        features = sp.audio_features(row['id'])[0]
        dat[i, 'Acousticness'] = features['acousticness']
        dat[i, 'Danceability'] = features['danceability']
        dat[i, 'Duration(s)'] = features['duration_ms'] / 1000
        dat[i, 'Energy'] = features['energy']
        dat[i, 'Wordiness'] = features['speechiness']
        dat[i, 'Tempo'] = features['tempo']
        dat[i, 'Positivity'] = features['valence']
        dat[i, 'Loudness'] = features['loudness']
        dat[i, 'Liveness'] = features['liveness']
        dat[i, 'Time Signature'] = features['time_signature']

#comment start for timeit
 #   df['Bumps in the whip?'] = pd.Series(banger.test(df)).values

#comment end for timeit
    return df 

def calc_avg(df):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for column in df.select_dtypes(include = numerics).columns:
        df.at['Total Average', column] = df[column].astype(float).mean()
    df.at['Total Average', 'track'] = ('Total Average')
    return df


#TESTING--------------------------------------
#
#def wrapper(func, *args, **kwargs):
#    def wrapped():
#        return func(*args, **kwargs)
#    return wrapped    
#
##wrapped = wrapper(search_album_id, "Saturation", "Brockhampton")
##wrappeddep = wrapper(search_album_id_deprecated, "Saturation", "Brockhampton")
#df = search_album_id("saturation", "brockhampton")
#print(df.head)
#wrapped = wrapper(assemble_df, df)
##wrappeddep = wrapper(assemble_df_deprecated, df)
#
#
#timed = timeit.timeit(wrapped, number=1);
##timeddep = timeit.timeit(wrappeddep, number=1);
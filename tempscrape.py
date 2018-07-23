import pandas as pd
import requests
import numpy as np
import re
import nltk
from textstat.textstat import textstat
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#nltk.download('vader_lexicon')
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import Counter


client_id = '91df6ca120d7407a877a64fabb100b49'
client_secret = '05a35b3ad63948c398d82dc8251d2bfb'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



def scrape_lyrics(title, artist):
    ##Takes the Url and strips the html down to just the lyrics
    ##The Lyrics are placed into var clean
    title = title.replace(" ", "-")
    title = title.replace("/", "-")
    title = title.replace("&", "and")
    title = re.sub('[^0-9a-zA-Z-]+', '', title)
    artist = artist.replace(" ", "-")
    artist = artist.replace("/", "-")
    artist = artist.replace("&", "and")
    artist = re.sub('[^0-9a-zA-Z-]+', '', artist)
    url = 'https://genius.com/'+artist+'-'+title+'-lyrics'
    source = requests.get(url)
    if source.status_code == 404:
        print('Error')
        raise Exception('Incorrect track or artist')
    source = source.text
    source = source.split('<div class="lyrics">')[1]
    source = source.split('<!--/sse-->')[0]
    clean = re.sub('<[^>]+>', '', source).strip()
    return clean

def sentiment_analysis(lyrics):
    #in future get rid of brackets that have artist name
   sid = SentimentIntensityAnalyzer()
   ss = sid.polarity_scores(lyrics)
   return ss['compound']
    

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
    rl = textstat.flesch_reading_ease(lyrics)
    return rl
#100.00-90.00 	5th grade 	Very easy to read. Easily understood by an average 11-year-old student.
#90.0–80.0 	6th grade 	Easy to read. Conversational English for consumers.
#80.0–70.0 	7th grade 	Fairly easy to read.
#70.0–60.0 	8th & 9th grade 	Plain English. Easily understood by 13- to 15-year-old students.
#60.0–50.0 	10th to 12th grade 	Fairly difficult to read.
#50.0–30.0 	College 	Difficult to read.
#30.0–0.0 	College graduate 	Very difficult to read. Best understood by university graduates. 

def search_song_id(title, artist):
    id_holder = {}
    search = title + ' ' + artist
    result = sp.search(q = search, limit = 1, type = 'track')
    result = result['tracks']
    result = result['items'][0]
    id_holder[title] = result['id']
    return id_holder

def search_album_id(album, artist):  
    id_holder = {}
    search = album + ' ' + artist
    result = sp.search(q = search, limit = 1, type = 'album')
    result = result['albums']
    result = result['items'][0]
    tracks = sp.album_tracks(result['id'])
    tracks = tracks['items']
    for item in tracks:
        id_holder[item['name']] = item['id']
    return id_holder
##InputGrabbers, commented out til GUI figured out
    ##title=Raw_Input('Song Title?')
    ##artist=Raw_Input('Artist name?')

def assemble_df(song_list):
    info = pd.DataFrame(columns = ('track',
                                   'lyrics',
                                   'sentiment',
                                   'syllables',
                                   'reading_level',
                                   'word_frequency',
                                   'acousticness',
                                   'danceability',
                                   'duration_ms',
                                   'energy',
                                   'speechiness',
                                   'tempo',
                                   'valence',
                                   'loudness',
                                   'liveness',
                                   'time_signature'
                                   ))
    
    for title in song_list.keys():
        holder = {}
        print(title)
        holder['track'] = title
        lyrics = scrape_lyrics(title, artist)
        holder['lyrics'] = lyrics
        holder['sentiment'] = sentiment_analysis(lyrics)
        holder['syllables'] = scansion_scanner(lyrics)
        holder['reading_level'] = reading_level(lyrics)
        holder['word_frequency'] = word_frequency(lyrics)
        features = sp.audio_features(song_list[title])[0]
        holder['acousticness'] = features['acousticness']
        holder['danceability'] = features['danceability']
        holder['duration_ms'] = features['duration_ms']
        holder['energy'] = features['energy']
        holder['speechiness'] = features['speechiness']
        holder['tempo'] = features['tempo']
        holder['valence'] = features['valence']
        holder['loudness'] = features['loudness']
        holder['liveness'] = features['liveness']
        holder['time_signature'] = features['time_signature']
        info = info.append(holder, ignore_index = True)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for column in info.select_dtypes(include = numerics).columns:
        info.at['Album average', column] = info[column].mean()
    return info
        
title = ''
album = 'kids see ghosts'
artist = 'kids see ghosts'
playlist = ''


if album != '':
    song_list = search_album_id(album, artist)
else:
    song_list = search_song_id(title, artist)

df = assemble_df(song_list)

    
    
#    analysis = sp.audio_analysis(id)
#    valence = valence_analysis(id)
#    mood = mood_analysis(lyrics, id)
    











import pandas as pd
import requests
import numpy as np
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
nltk.download('vader_lexicon')


def obtain_lyrics(url):
    ##Takes the Url and strips the html down to just the lyrics
    ##The Lyrics are placed into var clean
    source = requests.get(url).text
    source = source.split('<div class="lyrics">')[1]
    source = source.split('<!--/sse-->')[0]
    clean = re.sub('<[^>]+>', '', source).strip()
    return clean


def sentiment_analysis(lyrics):
    #in future get rid of brackets that have artist name
   sid = SentimentIntensityAnalyzer()
   ss = sid.polarity_scores(lyrics)
   return ss









##The Url for the song input
songtitle = 'look-at-me'
artist = 'xxxtentacion'
url = 'https://genius.com/'+artist+'-'+songtitle+'-lyrics'

lyrics = obtain_lyrics(url)
sentiment = sentiment_analysis(lyrics)










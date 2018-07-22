import pandas as pd
import requests
import numpy as np
import re
import nltk
from textstat.textstat import textstat
#not currently working bc module not found error and i die
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

def input_comber(title, artist):
    title = title.replace(" ", "-")
    artist = artist.replace(" ", "-")
    return

#This will need to run for each line separately, otherwise its useless
def scansion_scanner(lyrics):
    sc = textstat.syllable_count(lyrics)
    return sc

#decided which formula to use from documentation and this guide
#https://pypi.org/project/textstat/
#http://www.readabilityformulas.com/articles/how-do-i-decide-which-readability-formula-to-use.php
def reading_level(lyrics):
    rl = textstat.flesch_reading_ease(lyrics)
    return rl



##InputGrabbers, commented out til GUI figured out
    ##title=Raw_Input('Song Title?')
    ##artist=Raw_Input('Artist name?')
##The Url for the song input
title = 'look-at-me'
artist = 'xxxtentacion'
url = 'https://genius.com/'+artist+'-'+title+'-lyrics'

lyrics = obtain_lyrics(url)
sentiment = sentiment_analysis(lyrics)
syllables = scansion_scanner(lyrics)










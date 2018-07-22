import pandas as pd
import requests
import numpy as np
import re
import nltk
from textstat.textstat import textstat
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#nltk.download('vader_lexicon')


def scrape_lyrics(title, artist):
    ##Takes the Url and strips the html down to just the lyrics
    ##The Lyrics are placed into var clean
    title = title.replace(" ", "-")
    artist = artist.replace(" ", "-")
    url = url = 'https://genius.com/'+artist+'-'+title+'-lyrics'
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
#100.00-90.00 	5th grade 	Very easy to read. Easily understood by an average 11-year-old student.
#90.0–80.0 	6th grade 	Easy to read. Conversational English for consumers.
#80.0–70.0 	7th grade 	Fairly easy to read.
#70.0–60.0 	8th & 9th grade 	Plain English. Easily understood by 13- to 15-year-old students.
#60.0–50.0 	10th to 12th grade 	Fairly difficult to read.
#50.0–30.0 	College 	Difficult to read.
#30.0–0.0 	College graduate 	Very difficult to read. Best understood by university graduates. 


##InputGrabbers, commented out til GUI figured out
    ##title=Raw_Input('Song Title?')
    ##artist=Raw_Input('Artist name?')
title = 'look at me'
artist = 'xxxtentacion'


lyrics = scrape_lyrics(title, artist)
sentiment = sentiment_analysis(lyrics)
syllables = scansion_scanner(lyrics)










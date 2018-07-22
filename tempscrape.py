import pandas as pd
import requests
import numpy as np
import re




def obtain_lyrics():
    ##Takes the Url and strips the html down to just the lyrics
    ##The Lyrics are placed into var clean
    source = requests.get(url).text
    source = source.split('<div class="lyrics">')[1]
    source = source.split('<!--/sse-->')[0]
    clean = re.sub('<[^>]+>', '', source).strip()



def sentiment_analysis():
    pass











url = 'https://genius.com/Eminem-river-lyrics'

##The Url for the song input
songtitle = 'River'
artist = 'Eminem'
url = 'https://genius.com/'+artist+'-'+songtitle+'-lyrics'



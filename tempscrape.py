import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re




def obtain_lyrics():
    source = requests.get(url).text
    source = source.split('<div class="lyrics">')[1]
    source = source.split('<!--/sse-->')[0]
    clean = re.sub('<[^>]+>', '', source).strip()



def sentiment_analysis():












url = 'https://genius.com/Eminem-river-lyrics'




import pandas as pd
import requests
import numpy as np
import re

##The Url for the song input
songtitle = 'River'
artist = 'Eminem'
url = 'https://genius.com/'+artist+'-'+songtitle+'-lyrics'

##Takes the Url and strips the html down to just the lyrics
##The Lyrics are placed into var clean
source = requests.get(url)
source = source.text

new = source.split('<div class="lyrics">')[1]
new = new.split('<!--/sse-->')[0]

clean = re.sub('<[^>]+>', '', new).strip()

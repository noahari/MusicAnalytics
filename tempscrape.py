import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re

url = 'https://genius.com/Eminem-river-lyrics'

source = requests.get(url)
source = source.text

new = source.split('<div class="lyrics">')[1]
new = new.split('<!--/sse-->')[0]

clean = re.sub('<[^>]+>', '', source).strip()

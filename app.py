# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:32:34 2018

@author: skhos
"""

import json
import data_scrape
from flask import Flask, render_template
import pandas as pd
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def index():
    song_list = data_scrape.search_song_id('zipper', 'brockhampton')
    df = data_scrape.assemble_df(song_list)
    df = df.drop(['track', 'lyrics', 'id', 'word_frequency'], 1)
 

        
    chart_data = df.to_dict(orient='records')
    data = json.dumps(chart_data)
    data = json.loads(data)   
    return render_template("index.html", data = data)


if __name__ == "__main__":
    app.run(debug=True)

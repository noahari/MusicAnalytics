# -*- coding: utf-8 -*-

import json
import data_scrape
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
import pandas as pd
import sys




@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
    
    if request.method == 'POST':  #this block is only entered when the form is submitted
        
        array = request.form['queue1']

        #code from main.py
    
    
        clean = df.astype(str)
        chart_data = clean.to_dict(orient='records')
        data = json.dumps(chart_data)
        data = json.loads(data)
        return render_template("index.html", data = data)
    
#        for items in array:
#            if (array[items][2] = 0):    
#                df = data_scrape.search_album_id(array[items][0], array[items][1])
#            else if (array[items][2] = 1):
#                df = data_scrape.search_album_id(array[items][0], array[items][1])    
        
    
        
#        clean = df.drop(['artist', 'id', 'lyrics', 'Word Frequency'], 1)
#        clean = clean.astype(str)
#
#        chart_data = clean.to_dict(orient='records')
#        data = json.dumps(chart_data)
#        data = json.loads(data)
#        return render_template("index.html", data = data)
    
    artist = 'brockhampton'
    album = 'saturation'
    df = data_scrape.search_album_id(album, artist)
    df = data_scrape.assemble_df_deprecated(df)
    clean = df.drop(['artist', 'id', 'lyrics', 'Word Frequency'], 1)
    clean = clean.astype(str)

    chart_data = clean.to_dict(orient='records')
    data = json.dumps(chart_data)
    data = json.loads(data)
    
    return render_template("index.html", data = data)#[{'Enter a song':1}])




if __name__ == "__main__":
    app.run(debug=True)





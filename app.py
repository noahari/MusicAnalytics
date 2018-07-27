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
from flask import request
app = Flask(__name__)




@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        album = request.form.get('album')
        artist = request.form['artist']
        
        song_list = data_scrape.search_album_id(album, artist)
        df = data_scrape.assemble_df(song_list)
        df = df.drop(['lyrics', 'id', 'word_frequency'], 1)
     
        df = df.astype(str)
            
        chart_data = df.to_dict(orient='records')
        data = json.dumps(chart_data)
        data = json.loads(data)   
        return render_template("index.html", data = data)
        

    return '''<form method="POST">
                  album: <input type="text" name="album"><br>
                  artist: <input type="text" name="artist"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''





if __name__ == "__main__":
    app.run(debug=True)

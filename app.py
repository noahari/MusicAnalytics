# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:32:34 2018

@author: skhos
"""

import json
import data_scrape
from flask import Flask, render_template
from flask import request
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
    
    if request.method == 'POST':  #this block is only entered when the form is submitted
        album = request.form.get('album')
        artist = request.form['artist']

        df = data_scrape.search_album_id(album, artist)
        df = data_scrape.assemble_df(df)

        clean = df.drop(['artist', 'id', 'lyrics', 'Word Frequency'], 1)
        clean = clean.astype(str)

        chart_data = clean.to_dict(orient='records')
        data = json.dumps(chart_data)
        data = json.loads(data)
        return render_template("index.html", data = data)
    
    return render_template("index.html", data = [{'Enter a song':1}])




if __name__ == "__main__":
    app.run(debug=True)





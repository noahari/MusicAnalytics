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
        df = pd.DataFrame(eval(request.form['queue1']))
        df2 = df[['artist', 'name', 'tf']].copy().dropna()
        df = df.drop(['name', 'tf'], 1).dropna()
        for i, row in df2.iterrows():
            if(row['tf'] == 0):
                df = pd.concat([df, data_scrape.assemble_df(data_scrape.search_album_id(row['name'],row['artist']))])
            else:
                df = pd.concat([df, data_scrape.assemble_df(data_scrape.search_song_id(row['name'],row['artist']))])               
        try:
            df = df.drop('Enter a song', 1).dropna()
        except:
            pass
        return render_template("index.html", data = json.loads(json.dumps(df.drop(['id', 'lyrics', 'Word Frequency'], 1).astype(str).to_dict(orient='records'))))
    return render_template("index.html", data = [{'Enter a song':1}])

if __name__ == "__main__":
    app.run(debug=True)





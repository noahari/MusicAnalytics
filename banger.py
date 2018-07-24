# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib




def train():
    #term frequency inverse document frequency
    #svm model to assign banger or not
    song_list = {}
    df = pd.read_csv('train_data.csv')
    for i, row in df.iterrows():
        print(row['Title'])
        song_list = dict(list(song_list.items()) + list(data_scrape.search_song_id(row['Title'], row['Artist']).items()))
    total = data_scrape.assemble_df(song_list)
    total = total.drop('Album average', 0)
    clf = RandomForestClassifier()
    clf.fit(total.drop(['track', 'lyrics', 'id', 'word_frequency'], 1), df['Label'])
    joblib.dump(clf, 'rf_model.pkl') 
    
def percent_bangitude(title, artist):
    songid = data_scrape.search_song_id(title, artist)
    songdata = data_scrape.assemble_df(songid)
    energy = float(np.float64(songdata.at(0,'energy')).item())
    danceability = float(np.float64(songdata.get_value(0,'danceability')).item())
    bangitude = energy + danceability
    bangitude = str((round((bangitude/2)*100,2)))
    print('This song is '+bangitude+'% bangin')
    return
    
def test(title, artist, albool):
    clf = joblib.load('rf_model.pkl')
    if albool == 1:
        song_list = data_scrape.search_album_id(title, artist)
    else:
        song_list = data_scrape.search_song_id(title, artist)
    total = data_scrape.assemble_df(song_list)
    total = total.drop(['track', 'lyrics', 'id', 'word_frequency'], 1)
    if albool == 1:
        total = total.drop('Album average', 0)
        output = []
        #the present error is likely here, due to clf.predict recieving 
        #an incorrectly shaped array, possibly due to handing it a row instead of a df
        #possible solution: convert index in loop to df data type before clf.predict
        for index,row in total.iterrows():
            output.append(clf.predict(row))
        finout = float(sum(output))/float(len(output))
        #return finout+'% Banger Album'
        if finout > .5:
            return 'banger'
        else:
            return 'soft'
    else:    
        output = clf.predict(total)
        if output == 1:
            return 'banger'
        else:
            return 'soft'
        
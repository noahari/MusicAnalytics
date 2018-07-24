# -*- coding: utf-8 -*-
import pandas as pd
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
    bangitude = songdata['energy'] + songdata['danceability']
    bangitude = (bangitude/2)*100
    return 'This song is '+bangitude+'% bangin'
    
def test(title, artist, albool):
    clf = joblib.load('rf_model.pkl')
    if albool == 1:
        song_list = data_scrape.search_album_id(title, artist)
    else:
        song_list = data_scrape.search_song_id(title, artist)
    total = data_scrape.assemble_df(song_list)
    #total = total.drop('Album average', 0)
    total = total.drop(['track', 'lyrics', 'id', 'word_frequency'], 1)
    if albool == 1:
        output = []
        acc = 0
        for song in total:
            output = output.append(clf.predict(song))
        for bools in output:
            acc = acc + bools
        finout = acc/len(output)
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
        
#testvar = percent_bangitude('Yonkers','Tyler the creator')
#print(testvar)
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
    
            

def test(title, artist):
    clf = joblib.load('rf_model.pkl')
    song_list = data_scrape.search_song_id(title, artist)
    total = data_scrape.assemble_df(song_list)
    total = total.drop('Album average', 0)
    output = clf.predict(total.drop(['track', 'lyrics', 'id', 'word_frequency'], 1))
    if output == 1:
        return 'banger'
    else:
        return 'soft'


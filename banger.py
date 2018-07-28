# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler




def train():
    df = pd.read_csv('train_data.csv')
    df['id'] = df.apply(lambda row: data_scrape.search_song_id(row['track'], row['artist']), 1 )
    df = data_scrape.assemble_df(df)
    df = df.drop('Album Average', 0)
    test_df = df.drop(['track', 'artist', 'Label', 'id', 'lyrics', 'Word Frequency'], 1)
    scaler = StandardScaler()
    test_df = scaler.fit_transform(test_df)
    clf = RandomForestClassifier()
    clf.fit(test_df, df['Label'])
    joblib.dump(clf, 'rf_model.pkl') 
    joblib.dump(scaler, 'scaler.pkl') 
    
def percent_bangitude(title, artist):
    
    songid = data_scrape.search_song_id(title, artist)
    songdata = data_scrape.assemble_df(songid)
    energy = float(np.float64(songdata.get_value(0,'energy')).item())
    danceability = float(np.float64(songdata.get_value(0,'danceability')).item())
    bangitude = energy + danceability
    bangitude = str((round((bangitude/2)*100,2)))
    print('This song is '+bangitude+'% bangin')
    return

    
def test(df):
    scaler = joblib.load('scaler.pkl')
    clf = joblib.load('rf_model.pkl')
    test_df = df.drop(['track', 'artist', 'id', 'lyrics', 'Word Frequency'], 1)
    test_df = scaler.transform(test_df)
    return clf.predict(test_df)

        
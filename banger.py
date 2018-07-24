# -*- coding: utf-8 -*-
import pandas as pd
import data_scrape




def train():
    #term frequency inverse document frequency
    #svm model to assign banger or not
    song_list = {}
    df = pd.read_csv('train_data.csv')
    for i, row in df.iterrows():
        print(row['Artist'])
        song_list = data_scrape.search_song_id(row['Title'], row['Artist']) 
    print(song_list)
    df = data_scrape.assemble_df(song_list)
    
    
    
    
    return df

def test():
    #random forest classifer
    pass


train()
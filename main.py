
import banger
import data_scrape
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler




        
album = 'saturation'
artist = 'brockhampton'
playlist = ''

'''
if title != '':
    song_list = data_scrape.search_album_id(title, artist)
else:
    song_list = data_scrape.search_song_id(title, artist)

#df = data_scrape.assemble_df(song_list, artist)

banger_or_nah = banger.test(title, artist, 1)
'''
#    analysis = sp.audio_analysis(id)
#    valence = valence_analysis(id)
#    mood = mood_analysis(lyrics, id)
    
#testdf = data_scrape.assemble_df(data_scrape.search_song_id(title, artist))
#testval = testdf.at(0,'energy')
#print(testval)
#data_scrape.print_df(data_scrape.assemble_df(data_scrape.search_song_id(title, artist)))


array = [{"Enter a song":1},{"name":"views","artist":"drake","tf":0}]
df = pd.DataFrame(array)
df2 = df[['artist', 'name', 'tf']].copy().dropna()
df = df.drop(['artist', 'name', 'tf'], 1).dropna()
for i, row in df2.iterrows():
    if(row['tf'] == 0):
        temp = data_scrape.search_album_id(row['name'],row['artist'])
    else:
        temp = data_scrape.search_song_id(row['name'],row['artist'])
    temp = data_scrape.assemble_df(temp)
    df = pd.concat([df, temp])
try:
    df = df.drop('Enter a song', 1).dropna()
except:
    pass
#data_scrape.calc_avg(df)
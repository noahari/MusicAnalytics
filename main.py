
import banger
import data_scrape




        
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


song_list = data_scrape.search_album_id(album, artist)
df = data_scrape.assemble_df(song_list)
df = df.drop(['lyrics', 'id', 'word_frequency'], 1)
for i, row in df.drop('Album average', 0).iterrows():
    df.at[i,'Bumps in the whip'] = True if banger.test(row['track'], artist, 0) == 1 else False
df.at['Album average', 'track'] = album + str(' average')

df = df.astype(str)



chart_data = df.to_dict(orient='records')







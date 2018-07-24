
import banger
import data_scrape




        
title = 'in tongues'
album = ''
artist = 'joji'
playlist = ''


if album != '':
    song_list = data_scrape.search_album_id(album, artist)
else:
    song_list = data_scrape.search_song_id(title, artist)

#df = data_scrape.assemble_df(song_list, artist)

banger_or_nah = banger.test(title, artist, 1)
    
#    analysis = sp.audio_analysis(id)
#    valence = valence_analysis(id)
#    mood = mood_analysis(lyrics, id)
    
#testdf = data_scrape.assemble_df(data_scrape.search_song_id(title, artist))
#testval = testdf.at(0,'energy')
#print(testval)
#data_scrape.print_df(data_scrape.assemble_df(data_scrape.search_song_id(title, artist)))









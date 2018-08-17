
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


array = [{"Acousticness":"0.0137","Bumps in the whip?":"1.0","Danceability":"0.604","Duration(s)":"193.155","Energy":"0.933","Liveness":"0.37","Loudness":"-3.034","Lyrical Sentiment":"-0.9975","Positivity":"0.28","Reading Level":"14.7","Tempo":"110.029","Time Signature":"4.0","Verbosity":"0.214","track":"BOOGIE"},{"Acousticness":"0.249","Bumps in the whip?":"1.0","Danceability":"0.835","Duration(s)":"202.087","Energy":"0.681","Liveness":"0.18","Loudness":"-4.357","Lyrical Sentiment":"-0.983","Positivity":"0.687","Reading Level":"52.0","Tempo":"113.989","Time Signature":"4.0","Verbosity":"0.111","track":"ZIPPER"},{"Acousticness":"0.442","Bumps in the whip?":"0.0","Danceability":"0.612","Duration(s)":"251.909","Energy":"0.858","Liveness":"0.205","Loudness":"-5.359","Lyrical Sentiment":"0.9889","Positivity":"0.869","Reading Level":"75.8","Tempo":"80.352","Time Signature":"4.0","Verbosity":"0.364","track":"JOHNNY"},{"Acousticness":"0.423","Bumps in the whip?":"1.0","Danceability":"0.639","Duration(s)":"82.286","Energy":"0.631","Liveness":"0.709","Loudness":"-5.98","Lyrical Sentiment":"0.9057","Positivity":"0.531","Reading Level":"45.2","Tempo":"140.121","Time Signature":"4.0","Verbosity":"0.107","track":"LIQUID"},{"Acousticness":"0.935","Bumps in the whip?":"1.0","Danceability":"0.495","Duration(s)":"45.591","Energy":"0.264","Liveness":"0.16","Loudness":"-17.237","Lyrical Sentiment":"0.0","Positivity":"0.322","Reading Level":"16.5","Tempo":"81.74","Time Signature":"4.0","Verbosity":"0.223","track":"CINEMA 1"},{"Acousticness":"0.117","Bumps in the whip?":"1.0","Danceability":"0.773","Duration(s)":"216.715","Energy":"0.489","Liveness":"0.163","Loudness":"-6.025","Lyrical Sentiment":"0.8474","Positivity":"0.596","Reading Level":"102.9","Tempo":"69.985","Time Signature":"4.0","Verbosity":"0.141","track":"STUPID"},{"Acousticness":"0.462","Bumps in the whip?":"1.0","Danceability":"0.595","Duration(s)":"273.151","Energy":"0.657","Liveness":"0.437","Loudness":"-6.498","Lyrical Sentiment":"0.7993","Positivity":"0.718","Reading Level":"13.1","Tempo":"156.093","Time Signature":"4.0","Verbosity":"0.183","track":"BLEACH"},{"Acousticness":"0.12","Bumps in the whip?":"1.0","Danceability":"0.721","Duration(s)":"199.195","Energy":"0.603","Liveness":"0.936","Loudness":"-6.705","Lyrical Sentiment":"-0.9729","Positivity":"0.405","Reading Level":"66.4","Tempo":"75.018","Time Signature":"4.0","Verbosity":"0.272","track":"ALASKA"},{"Acousticness":"0.163","Bumps in the whip?":"1.0","Danceability":"0.856","Duration(s)":"197.148","Energy":"0.712","Liveness":"0.123","Loudness":"-6.355","Lyrical Sentiment":"0.9864","Positivity":"0.774","Reading Level":"46.1","Tempo":"128.994","Time Signature":"4.0","Verbosity":"0.0621","track":"HOTTIE"},{"Acousticness":"0.803","Bumps in the whip?":"0.0","Danceability":"0.422","Duration(s)":"38.617","Energy":"0.371","Liveness":"0.36","Loudness":"-17.12","Lyrical Sentiment":"-0.2263","Positivity":"0.707","Reading Level":"29.0","Tempo":"103.174","Time Signature":"4.0","Verbosity":"0.087","track":"CINEMA 2"},{"Acousticness":"0.0917","Bumps in the whip?":"1.0","Danceability":"0.378","Duration(s)":"364.637","Energy":"0.691","Liveness":"0.0557","Loudness":"-7.263","Lyrical Sentiment":"-0.999","Positivity":"0.508","Reading Level":"49.7","Tempo":"150.134","Time Signature":"4.0","Verbosity":"0.224","track":"SISTER/NATION"},{"Acousticness":"0.194","Bumps in the whip?":"0.0","Danceability":"0.672","Duration(s)":"213.659","Energy":"0.452","Liveness":"0.251","Loudness":"-7.947","Lyrical Sentiment":"-0.5447","Positivity":"0.514","Reading Level":"223.2","Tempo":"82.012","Time Signature":"4.0","Verbosity":"0.0738","track":"RENTAL"},{"Acousticness":"0.474","Bumps in the whip?":"1.0","Danceability":"0.643","Duration(s)":"179.151","Energy":"0.662","Liveness":"0.237","Loudness":"-7.226","Lyrical Sentiment":"-0.9812","Positivity":"0.645","Reading Level":"46.7","Tempo":"113.022","Time Signature":"4.0","Verbosity":"0.0993","track":"STAINS"},{"Acousticness":"0.905","Bumps in the whip?":"0.0","Danceability":"0.356","Duration(s)":"51.206","Energy":"0.335","Liveness":"0.162","Loudness":"-17.477","Lyrical Sentiment":"0.6124","Positivity":"0.389","Reading Level":"54.0","Tempo":"120.817","Time Signature":"4.0","Verbosity":"0.0549","track":"CINEMA 3"},{"Acousticness":"0.396","Bumps in the whip?":"1.0","Danceability":"0.312","Duration(s)":"273.682","Energy":"0.73","Liveness":"0.942","Loudness":"-7.433","Lyrical Sentiment":"0.9286","Positivity":"0.267","Reading Level":"20.7","Tempo":"140.099","Time Signature":"4.0","Verbosity":"0.126","track":"TEAM"},{"Acousticness":"0.38589333333333337","Bumps in the whip?":"0.7333333333333333","Danceability":"0.5942000000000001","Duration(s)":"185.4792666666667","Energy":"0.6046","Liveness":"0.35271333333333327","Loudness":"-8.401066666666669","Lyrical Sentiment":"0.024273333333333348","Positivity":"0.5474666666666668","Reading Level":"57.06666666666668","Tempo":"111.0386","Time Signature":"4.0","Verbosity":"0.15614","track":"Album Average"},{"name":"views","artist":"drake","tf":0}]
df = pd.DataFrame(array)
df2 = df[['artist', 'name', 'tf']].copy().dropna()
df = df.drop(['artist', 'name', 'tf'], 1).dropna()
for i, row in df2.iterrows():
    if(row['tf'] == 0):
        data_scrape.search_album_id
    else:
        data_scrape.search_song_id

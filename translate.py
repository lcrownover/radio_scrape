import sqlite3

# ['artist','song','playdate']
songs_list = []
with open('./songs_played.txt', 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))


# Connect to db
conn = sqlite3.connect('songs.db')
c = conn.cursor()


song_names = [i[1] for i in songs_list]
artist_names = [i[0] for i in songs_list]

def append_song_table():
    unique_songs = []
    for song_name in song_names:
        if song_name not in unique_songs:
            unique_songs.append(song_name)
        
    for song_name in unique_songs:
        c.execute("INSERT INTO SONGS (NAME) VALUES (\"{}\");".format(str(song_name)))

    conn.commit()

def append_artist_table():
    unique_artists = []
    for artist_name in artist_names:
        if artist_name not in unique_artists:
            unique_artists.append(artist_name)
        
    for artist_name in unique_artists:
        c.execute("INSERT INTO ARTISTS (NAME) VALUES (\"{}\");".format(str(artist_name)))

    conn.commit()



append_song_table()
append_artist_table()

conn.close()





# unique_dict = {}
# for song_name in song_names:
#     if song_name not in unique_dict:
#         unique_dict[song_name] = {'count': 1}
#     else:
#         unique_dict[song_name]['count'] += 1

# for k,v in unique_dict.items():
#     print(k,v)
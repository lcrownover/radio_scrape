import sqlite3



# Connect to db
conn = sqlite3.connect('radio_songs.db')
c = conn.cursor()

# ['artist','song','playdate']
songs_list = []
with open('./songs_played.txt', 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))

#song_names = [i[1] for i in songs_list]     # ['songname1','songname2']
#artist_names = [i[0] for i in songs_list]   # ['artistname1','artistname2']
#playdate = [i[2] for i in songs_list]       

def add_data():
    for play in songs_list:
        artist_name = play[0]
        song_name = play[1]
        playdate = play[2]
        
        #print("artist: {}, song: {}, date played: {}".format(artist_name,song_name,playdate))
        c.execute('''SELECT * FROM artists WHERE artist_name=?''', (artist_name,))
        artist_present = c.fetchone()
        print(artist_present)
        if not artist_present:
            c.execute('''INSERT INTO artists(artist_name) VALUES(?)''', (artist_name,))
        

        c.execute('''SELECT * FROM songs WHERE song_name=?;''', (song_name,))
        song_present = c.fetchone()
        print(song_present)
        if not song_present:
            c.execute('''SELECT artist_id FROM artists WHERE artist_name=?''', (artist_name,))
            artist_id = c.fetchone()
            c.execute('''INSERT INTO songs (song_name, artist_id) VALUES (?,?);''', (song_name, artist_id))

        conn.commit()



def append_artists_table():
    unique_artists = []
    for artist_name in artist_names:
        if artist_name not in unique_artists:
            unique_artists.append(artist_name)
        
    for artist_name in unique_artists:
        c.execute("INSERT INTO ARTISTS (ARTIST_NAME) VALUES (\"{}\");".format(str(artist_name)))

    conn.commit()

def append_songs_table():
    unique_songs = []
    for song_name in song_names:
        if song_name not in unique_songs:
            unique_songs.append(song_name)
        
    for song_name in unique_songs:
        c.execute("INSERT INTO SONGS (SONG_NAME) VALUES (\"{}\");".format(str(song_name)))

    conn.commit()

# def append_playdates_table():
#     unique_artists = []
#     for artist_name in artist_names:
#         if artist_name not in unique_artists:
#             unique_artists.append(artist_name)
        
#     for artist_name in unique_artists:
#         c.execute("INSERT INTO ARTISTS (NAME) VALUES (\"{}\");".format(str(artist_name)))

#     conn.commit()



#append_songs_table()
#append_artists_table()

add_data()

conn.close()





# unique_dict = {}
# for song_name in song_names:
#     if song_name not in unique_dict:
#         unique_dict[song_name] = {'count': 1}
#     else:
#         unique_dict[song_name]['count'] += 1

# for k,v in unique_dict.items():
#     print(k,v)
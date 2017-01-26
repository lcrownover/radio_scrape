import sqlite3


#files
songs_db = '/opt/radio_scrape/db/radio_songs.db'
songs_file = '/opt/radio_scrape/log/songs_played.txt'

# Connect to db
conn = sqlite3.connect(songs_db)
c = conn.cursor()

# ['artist','song','playdate']
songs_list = []
with open(songs_file, 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))    

for play in songs_list:
    artist_name = play[0]
    song_name = play[1]
    playdate = play[2]
    
    # inserts artists into artists table
    c.execute('SELECT * FROM artists WHERE artist_name=?', (artist_name,))
    artist_present = c.fetchone()
    if not artist_present:
        print('New Artist!: {}'.format(artist_name))
        c.execute('INSERT INTO artists(artist_name) VALUES(?)', (artist_name,))
    
    # inserts songs into songs table
    c.execute('SELECT * FROM songs WHERE song_name=?;', (song_name,))
    song_present = c.fetchone()
    if not song_present:
        print('New Song from {}!: {}'.format(artist_name, song_name))
        c.execute('SELECT artist_id FROM artists WHERE artist_name=?', (artist_name,))
        artist_id = str(c.fetchone()[0])
        c.execute('INSERT INTO songs (song_name, artist_id) VALUES (?,?)', (song_name, artist_id))

    # inserts playdates into playdates table
    c.execute('SELECT song_id FROM songs WHERE song_name=?', (song_name,))
    song_id = str(c.fetchone()[0])
    c.execute('INSERT INTO playdates (song_id, datetime) VALUES (?,?)', (song_id, playdate))


conn.commit()
conn.close()

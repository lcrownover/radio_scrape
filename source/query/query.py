import sqlite3


#database
songs_db = '/opt/radio_scrape/db/radio_songs.db'

# Connect to db
conn = sqlite3.connect(songs_db)
c = conn.cursor()

c.execute('SELECT datetime FROM playdates')
playdates = c.fetchall()

last_date = ''

for date in playdates:
    date = sorted(''.join(date).split(' ')[1][:5])
    if date == last_date:
        print('found duplicate')
    


conn.close()

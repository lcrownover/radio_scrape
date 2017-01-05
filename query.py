import sqlite3


#database
songs_db = '/home/lucasc/code/projects/radio_scrape/radio_songs.db'

# Connect to db
conn = sqlite3.connect(songs_db)
c = conn.cursor()

c.execute('SELCT * FROM playdates')
playdates = c.fetchall()

for date in playdates:
    print(date)


conn.close()
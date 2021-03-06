#!/usr/bin/python3

import time
import datetime
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_playlist_history():    
    #returns list of songs
    
    html = urlopen("http://www.stations.xyz/radio/player/293")
    soup = BeautifulSoup(html, "html.parser")
    home_playlist_raw = soup.find(id = "home_playlist")

    songs = re.sub(pattern_html, '~~', str(home_playlist_raw).strip())
    songs = songs.strip().split('~~~~')
    songs = list(filter(None, songs))

    return songs

def log_data(data):
   debug = '/opt/radio_scrape/log/debug.txt'
   with open(debug, 'a') as f:
      f.write("{}\n".format(data))

#regex patterns
pattern_html = r"(\<div id\=[\"\']\w+[\"\']\>\n)|(\<\/p\>)|(\<p\>)|(\n\<\/div\>)"
pattern_song_artist = r'(\s\-\s?)'

#main output file
log = '/opt/radio_scrape/log/songs_played.txt' 

start_time = time.time()

#set a working list that will persist outside while loop
persist_list = get_playlist_history()

never_stop = True

while never_stop:
    #wrap whole program in timer

    time_now = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    log_data('time now: '+time_now)

    new_list = get_playlist_history()
    #replaces song/artist delimiter with more easily splittable pattern
    song_artist = re.sub(pattern_song_artist, ' ~~ ', str(new_list[0].strip()))

    log_data(persist_list[0])
    log_data(new_list[0])

    if persist_list[0] != new_list[0]:
        #add entry to log
        with open(log, 'a') as f:
            f.write("{} ~~ {} \n".format(song_artist, time_now))
            
        persist_list = new_list
        log_data('added entry!')
    
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))

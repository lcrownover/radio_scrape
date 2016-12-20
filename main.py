#!/usr/bin/python3

import time
import datetime
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tinydb import TinyDB, where

def get_songs():    
    #returns list of songs
    
    html = urlopen("http://www.stations.xyz/radio/player/293")
    soup = BeautifulSoup(html, "lxml")
    home_playlist_raw = soup.find(id = "home_playlist")

    p = r"(\<div id\=[\"\']\w+[\"\']\>\n)|(\<\/p\>)|(\<p\>)|(\n\<\/div\>)"
    songs = re.sub(p, '~~', str(home_playlist_raw).strip())
    songs = songs.strip().split('~~~~')
    songs = list(filter(None, songs))

    return songs

db = TinyDB('./db.json')
table = db.table('bobfm')
start_time = time.time()
persist_list = get_songs()

while True:
    #wrap whole program in timer

    time_now = str(datetime.datetime.now())
    new_list = get_songs()
    if persist_list[0] == new_list[0]:
        print(new_list[0])        
    else:
        print(new_list[0] + '  - new song! inserted into database.')
        table.insert({'song': new_list[0], 'datetime': time_now})
    persist_list = new_list
    
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))
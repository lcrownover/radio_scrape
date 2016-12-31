#!/bin/bash
cp ./cron.sh /etc/cron.daily
database="./radio_songs.db"
if [[ ! -f $target ]]; then 
    sqlite3 radio_songs.db < schema.sql
fi
nohup python3 main.py &>/dev/null &
#!/bin/bash
cp -rf ./radio_scrape_cron.sh /etc/cron.daily
chmod +x /etc/cron.daily/radio_scrape_cron.sh
database="./radio_songs.db"
if [[ ! -f $database ]]; then 
    sqlite3 radio_songs.db < schema.sql
fi
nohup python3 main.py &>/dev/null &
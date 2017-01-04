#!/bin/bash

cp -rf ./radio_scrape_cron /etc/cron.daily
chmod +x /etc/cron.daily/radio_scrape_cron
echo "Cron files copied"

echo "Checking database..."
database="./radio_songs.db"
if [[ ! -f $database ]]; then
    sqlite3 radio_songs.db < schema.sql
    chown lucasc:lucasc radio_songs.db
    echo "Database not found, new one created."
fi

pid="$(ps axf | grep main.py | grep -v grep | awk '{print$1}')"
nohup python3 main.py &>/dev/null &
echo -e "Process started with pid $pid" 

#!/bin/bash

cd /opt/radio_scrape

# Copying service file to systemd directory
cp -rf ./src/radio_scrape.service /lib/systemd/system/radio_scrape.service
chmod +x /lib/systemd/system/radio_scrape.service
echo "Service 'radio_scrape.service' created"

# Copying cron file to cron.daily
cp -rf ./src/radio_scrape_cron /etc/cron.daily
chmod +x /etc/cron.daily/radio_scrape_cron
echo "Cron files copied"

# Checking to see if database exists
database="./db/radio_songs.db"
if [[ ! -f $database ]]; then
    sqlite3 ./db/radio_songs.db < ./db/schema.sql
    chown lucasc:lucasc ./db/radio_songs.db
    echo "Database not found, new one created."
fi
echo "Database found"

# Check to see if service is enabled and starts it
servicelink="/etc/systemd/system/radio_scrape.service"
if [[ ! -L $servicelink ]]; then
    systemctl enable radio_scrape.service > /dev/null 2>$1
fi
systemctl start radio_scrape.service
echo "Service started"

# Print PID of process to console
# pid="$(ps axf | grep main.py | grep -v grep | awk '{print$1}')"
# echo -e "Process started with pid $pid" 

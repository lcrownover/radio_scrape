cp ./cron.sh /etc/cron.daily
database="./radio_songs.db"
if [[ ! -f $target ]]; then 
    sqlite3 radio_songs.db < schema.sql
nohup python3 main.py &>/dev/null &
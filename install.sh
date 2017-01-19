#!/bin/bash

mkdir /opt/radio_scrape
cp -rp ./source/* /opt/radio_scrape
bash /opt/radio_scrape/run.sh

echo "radio_scrape installed to /opt/radio_scrape"

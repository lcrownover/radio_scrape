#!/usr/bin/python3

import re

with open('./songs_played.txt', 'r') as f:

    songs_list = []
    p = r"(\s\\n)|(\\n)"

    for line in f.readlines():

        #trims newline characters from end of datetime
        line = re.sub(p, '', str(line))
        
        songs_list.append(line.split(" ~~ "))
        
    print(songs_list)
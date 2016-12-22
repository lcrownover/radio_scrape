#!/usr/bin/python3

with open('./songs_played.txt', 'r') as f:

    songs_list = []

    for line in f.readlines():
        songs_list.append(line.split(" ~~ "))
        
    print(songs_list)
#!/usr/bin/python3

songs_list = []

with open('./songs_played.txt', 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))



def get_song_play_count():
    song_names = [i[0] for i in songs_list]

    unique_songs = []
    for song in song_names:
        if song not in unique_songs:
            unique_songs.append(song)

    for i in unique_songs:
        print(i)

get_song_play_count()
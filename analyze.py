#!/usr/bin/python3

songs_list = []

with open('./songs_played.txt', 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))



def get_song_play_count():
    song_names = [i[0] for i in songs_list]

    unique_list = [[]]
    for song_name in song_names:
        if song_name not in unique_list:
            unique_list.append([song_name, 1])
        elif song_name in [song_name[0] for song_name in unique_list]:
            unique_list[song_name][1] + 1
    for i in sorted(unique_list):
        print(i)


    print("\n\n\n")
    for i in sorted(song_names):
        print(i)

get_song_play_count()
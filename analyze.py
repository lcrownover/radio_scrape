#!/usr/bin/python3

songs_list = []

with open('./songs_played.txt', 'r') as f:
    for line in f.readlines():
        songs_list.append(line.rstrip().split(" ~~ "))



def get_song_play_count():
    song_names = [i[0] for i in songs_list]

    unique_dict = {}
    for song_name in song_names:
        if song_name not in unique_dict:
            unique_dict[song_name] = {'count': 1}
        else:
            unique_dict[song_name]['count'] += 1

    for k,v in unique_dict.items():
        print(k,v)


    # print("\n\n\n")
    # for i in sorted(song_names):
    #     print(i)

get_song_play_count()
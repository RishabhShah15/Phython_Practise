song_durations=[60,120,180,240,300]
new_list=[]
for i in enumerate(song_durations,start=1):
    new_list.extend(i)
    print(i)
print(new_list)
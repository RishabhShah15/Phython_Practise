play_list=["101","102","103","104","105"]

#play_list1=["106","107","108"]

# print(play_list,id(play_list),type(play_list))

play_list.append('106')
print(play_list,id(play_list))
play_list.extend([107,108])
print(play_list,id(play_list))

play_list.pop()

print(play_list)
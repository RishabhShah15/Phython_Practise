def print_playlist_songs(songs):
    
    if not  songs:
        return
    print(songs[0])

    print_playlist_songs(songs[1:]) 



my_playlist = ["Blinding Lights", "Shape of You", "Dance Monkey", "Stay"]

print_playlist_songs(my_playlist)
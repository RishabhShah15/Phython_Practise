#Read the playlist.txt file you created and display each song name in uppercase letters using Python.
file=open('C:\\Python\session_14\\playlist.txt','r')
text=file.read()
print(text.upper())
file.close()
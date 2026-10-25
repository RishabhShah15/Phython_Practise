#Create a text file named playlist.txt and write the names of 5 songs you listened to this week,
#  each on a new line using Python's open() function in write mode.

file=open('C:\\Python\session_14\\playlist.txt','w')
file.write('Abcd')
file.write('\nBcd')
file.write('\nCdef')
file.write('\nDefg')
file.write('\nEfgh')
file.close()
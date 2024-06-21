#  Write a Python program to read an entire text file. 

def file_read(fname):
     txt = open(fname)
     print(txt.read())
        

file_read('q2.txt')
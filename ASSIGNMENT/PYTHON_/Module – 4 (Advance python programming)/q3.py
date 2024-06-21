#  Write a Python program to append text to a file and display the text.

def appen(file):
    file=open("q3.txt","a")
    file.write(add + "\n")
    file.close


add=input("enter taxt to append file:")
appen(add)

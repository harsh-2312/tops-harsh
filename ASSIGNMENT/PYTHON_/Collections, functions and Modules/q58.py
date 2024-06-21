# Write a Python program to read a random line from a file.  
import random

file=open("58.txt","r")
line=file.readlines()
print(random.choice(line))
file.close()



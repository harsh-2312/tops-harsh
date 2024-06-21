#  Write a Python program to count the number of lines in a text file. 

file_name='q4.txt'

def number(file_name):
    with open(file_name,'r') as file:
        count=len(file.readlines())
    return count
print(number(file_name))
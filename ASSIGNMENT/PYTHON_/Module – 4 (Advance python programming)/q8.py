# Write a python program to find the longest words.  
file_name='q8.txt'

def number(file_name):
    max_word=''
    with open(file_name,'r') as file:
        linse=file.read().split()
        for word in linse:
            if len(word) > len(max_word):
                max_word=word
    return max_word

print(number(file_name))
    
# Write a Python program to write a list to a file.  

names = ['Jessa', 'Eric', 'Bo','tom']


with open('q11.txt', 'w') as file:
    for i in names:
        file.write(i+"\n")

print('Done')



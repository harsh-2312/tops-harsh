# Write a Python program to read a file line by line store it into a variable. x
file_name="q4.txt"
def variable(file_name):
    with open(file_name,"r") as file:
        list_=file.readline()
        return list_
    
print(variable(file_name))



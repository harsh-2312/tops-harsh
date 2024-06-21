# Write a Python script to check if a given key already exists in a dictionary.

dic1={'h':1000,'a':333,'r':666,'s':66}
key=str(input("enter key:"))

if key in dic1:
    print(f"{key} is exists in a dictionary")
else:
    print(f"{key} is not exists in a dictionary")
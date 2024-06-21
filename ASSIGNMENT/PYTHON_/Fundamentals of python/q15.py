# Write a Python program to add 'ing' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then add 
# 'ly' instead if the string length of the given string is less than 3, leave it 
# unchanged.

str_=input("enter string:")

if len(str_) > 2:
    if str_.endswith("ing"):
        str_+="ly"
    else:
        str_+="ing"
print(str_)

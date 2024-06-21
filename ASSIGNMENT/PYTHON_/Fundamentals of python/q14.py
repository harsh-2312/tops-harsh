#  Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string. 

# before swaping
str_1=input("enter string1:")
str_2=input("enter string2:")


# after swaping

str_3=str_2[:2] + str_1[2:] + "   " + str_1[:2] + str_2[2:]

print(f"after swaping:{str_3}")
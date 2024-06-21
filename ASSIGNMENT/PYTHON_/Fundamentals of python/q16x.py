#  Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring with 'good'. Return the resulting string.

str1 = "The weather is not poor today."

not1=str1.find("not")
poor1=str1.find("poor")

re= str1.replace("not poor","good")

print(re)









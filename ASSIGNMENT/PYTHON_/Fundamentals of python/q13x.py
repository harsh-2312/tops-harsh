#  Write a Python program to count the occurrences of each word in a given sentence 

str1=input("enter string:").split()

final_data = []

un_word = list()
for ch in str1:
    if ch not in un_word:
        un_word.append(ch)
        final_data.append([ch,(str1.count(ch))])
print(final_data)

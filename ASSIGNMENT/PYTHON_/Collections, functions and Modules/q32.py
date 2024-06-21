# Write a Python script to sort (ascending and descending) a dictionary by value.

dic= {1:2,3:5,9:3,7:9}

ascend= sorted(dic.items(), key=lambda i: i[1])

descend= sorted(dic.items(), key=lambda i: i[1], reverse=True)

print("Ascending:", ascend)
print("Descending:", descend)

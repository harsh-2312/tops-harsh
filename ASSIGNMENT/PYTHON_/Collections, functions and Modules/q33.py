# Write a Python script to concatenate following dictionaries to create a new one.

dic1={'h':1,'a':2}
dic2={'r':5,'s':6}

new={}
for i in dic1,dic2:
    new.update(i)
print(new)
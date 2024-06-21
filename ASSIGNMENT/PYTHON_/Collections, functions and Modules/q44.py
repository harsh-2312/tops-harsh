# Write a Python program to create and display all combinations of letters, 
# selecting each letter from a different key in a dictionary. 
# Sample data: {'1': ['a','b'], '2': ['c','d']}  
# Expected Output:  ac ad bc bd  


dec1={'1': ['a','b'], '2': ['c','d']}  

data=[]

for i in dec1['1']:
    for j in dec1['2']:
        com=i+j

        data.append(com)
dec_string=' '.join(data)

print(dec_string)




















# for i in itertools.product(*[dec1[k] for k in sorted(dec1.keys())]):
#     print("".join(i))
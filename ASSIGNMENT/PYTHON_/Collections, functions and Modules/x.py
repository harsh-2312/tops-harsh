# Write a Python function to get the largest number, smallest num and sum 
# of all from a list.  

# lis=[1,2,3,4,5]
# m=max(lis)
# s=min(lis)
# ss=sum(lis)

# print(m,s,ss)

# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given 
# list of strings. 

# lis=['harh','raar','tom','sos']
# coun=0
# for i in lis:
#     if len(lis)>=2 and i[0]==i[-1]:
#         coun+=1
# print(coun)

# Write a Python program to remove duplicates from a list. 

# lis=[1,2,2,3,3,4,4,5]
# print(list(set(lis)))
# l=[]

# for i in lis:
#     if i not in l:
#         l.append(i)
# print(l)

# Write a Python program to check a list is empty or not. 

# lis=list(input("enter"))

# if len(lis)==0:
#     print("MT")
# else:
#     print("not Mt")

# Write a Python function that takes two lists and returns true if they have 
# at least one common member.  

# def ch(f,s):
#     res=False
#     for i in f:
#         for j in s:
#             if i==j:
#                 res = True
#     return res

# f=[1,2,3,4]
# s=[5,6,7,4]

# print(ch(f,s))


# lis=[]
# s=1

# for i in range(1,31):
#     s=i*i
#     lis.append(s)

# f=lis[:5]
# l=lis[-5:]

# print(f+l)

# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list. 

# def un(lis):
#     for i in lis:
#         if i not in u:
#             u.append(i)
#     return u


# lis=[1,2,3,4,5,5,4,3,2,1]
# u=[]

# print(un(lis))

# Write a Python program to convert a list of characters into a string. 


# lis=['h','r','e']

# re="".join(lis)

# print(re)

# Write a Python program to select an item randomly from a list.  

# import random

# lis=[1,5,3,4,2]

# print(random.choice(lis))

# Write a Python program to find the second smallest number in a list.  

# lis=[6,3,2,4,1]

# lis.sort()
# print(lis[1])

# Write a Python program to get unique values from a list  

# lis=[1,1,2,2,3,3,4,4]

# print(list(set(lis)))

# Write a Python program to check whether a list contains a sub list  

# def ch(lis,sub):
#     re=False
#     for i in range(len(lis)):
#         if lis[i:i + len(sub)]==sub:
#             re=True
#     return re
# lis=[1,2,3,4,5]
# sub=[2,3]

# print(ch(lis,sub))

#  Write a Python program to split a list into different variables.

# lis=['har','gsg','sjsh','hahah','sjsgfs']

# a,b,c,*d=lis

# print(a)
# print(b)
# print(c)
# print("".join(d))
# Write a Python program to create a tuple with different data types.

# tu=('hshsh',11,1.1,False,)
# print(tu)

# tu=tuple(input("enter"))

# print(tu)

# tu=(1,2,3,4)

# str(tu)
# print(tu)

# Write a Python program to check whether an element exists within a 
# tuple.  

# ch=int(input("num"))
# tup=(1,2,3,4)

# if ch  in tup:
#     print("yes")
# else:
#     print("no")

# Write a Python program to find the length of a tuple. 

# tup=(1,2,3,4,5)
# print(len(tup))

#  Write a Python program to convert a list to a tuple. 

# lis=[1,2,3,4,5]
# print(tuple(lis))

# Write a Python program to reverse a tuple. 

# tup=(1,2,3,4,5)

# re=tuple(reversed(tup))

# print(re)

# Write a Python program to replace last value of tuples in a list. 

# lis_tup=[(1,2,3),(4,5,6),(7,8,9)]

# new=[i[:-1]+(10,) for i in lis_tup]

# print(new)

# Write a Python program to find the repeated items of a tuple. 

# tup=(1,1,2,2,3,3,4,4,5,5)
# re=[]

# for i in tup:
#     if tup.count(i)>1:
#         if i not in re:
#             re.append(i)
# print(re)

# Write a Python program to remove an empty tuple(s) from a list of tuples. 

# lis=[(1,2),(),(1,3),()]

# for i in lis:
#     if len(i)==0:
#         lis.remove(i)
# print(lis)

# Write a Python program to remove an empty tuple(s) from a list of tuples. 

# list_tup=[(1,2,3),(4,5,6),()]

# for i in list_tup:
#     if (len(i)==0):
#         list_tup.remove(i)

# print(list_tup)

# Write a Python program to unzip a list of tuples into individual lists. 

# lis=[(1,2),(3,4),(5,6)]

# re=list(zip(*lis))
# print(re)

# Write a Python program to convert a list of tuples into a dictionary.  

# lis= [('h',1),('r',5)]

# new={key: value for key, value in lis}

# print(new)

# Write a Python script to sort (ascending and descending) a dictionary by 
# value. 

# dic= {1:2,3:5,9:3,7:9}

# asc=sorted(dic.items(),key=lambda i : i[1])
# de=sorted(dic.items(),key=lambda i : i[1],reverse=True)

# print(asc)
# print(de)

# Write a Python script to concatenate following dictionaries to create a 
# new one. 

# o={'h':3,'r':5}
# p={'g':4,'k':9}
# new={}

# for i in o,p:
#     new.update(i)
# print(new)

# Write a Python script to check if a given key already exists in a 
# dictionary. ~~~

# dic1={'h':1000,'a':333,'r':666,'s':66}

# ch=input("en")

# if ch in dic1:
#     print("yes")
# else:
#     print("no")

# n={}

# for key in range(1,16):
#     n[key]=key*key
# print(n)

# Write a Python program to check multiple keys exists in a dictionary 

# dic1={'h':1000,'a':333,'r':666,'s':66}

# print(dic1.keys() >= {'h','a'})

# Write a Python script to merge two Python dictionaries 

# dic1={'h':1000,'a':333}
# dic2={'r':666,'s':66}

# dic3={**dic1,**dic2}

# print(dic3)

# Write a Python program to map two lists into a dictionary  

# key=[1,2,3]
# value=[4,5,6]

# res=dict(zip(key,value))

# print(res)

#
# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200,'c':400}

# for i in d2:
#     if i in d1:
#         d2[i]=d2[i]+d1[i]
#     else:
#         pass

# print(d2)

# Write a Python program to print all unique values in a dictionary.  

# dic1={'a':10,'b':20,'c':30,'d':10,'e':20}

# re=set()

# for i in dic1.values():
#     re.add(i)
# print(re)



# dic1={'a':10,'b':20,'c':30,'d':10,'e':20}

# res= set()

# for i in dic1.values():
#     res.add(i)
# print(res)

# dic1={'a':10,'b':20,'c':30,'d':10,'e':20}

# ass=sorted(dic1.items(), key=lambda i : i[1])
# d=sorted(dic1.items(), key=lambda i : i[1], reverse=True)


# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'h': 300, 'o': 200,'k':400}

# new={}

# for i in d1,d2:
#     new.update(i)
# # print(new)
# Write a Python script to check if a given key already exists in a 
# dictionary.

# d1 = {'a': 100, 'b': 200, 'c':300} 
# key=input('enter')

# if key in d1:
#     print('y')
# else:
#     print('n')

# dec={}

# for i in range(1,16):
#     dec[i]=i
# # print("*")

# d1 = {'a': 100, 'b': 200, 'c':300} 

# print(d1.keys() >= {"a",'c'})

# d1 = ['a','r','y']
# d2 = [300,200,400]

# re=dict(zip(d1,d2))
# print(re)


# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200,'c':400}

# for i in d2:
#     if i in d1:
#         d2[i]=d2[i]+d1[i]
        
#     else:
#         pass
# print(d2)

# d1 = {'a': 100, 'b': 200, 'c':300,'a': 300, 'b': 200,'c':400}

# un=set()

# for i in d1.keys():
#     un.add(i)
# print(un)

# data= {'1': ['a','b'], '2': ['c','d']} 
# s=[]

# for i in data['1']:
#     for j in data['2']:
#         com=i+j
#         s.append(com)
# l=" ".join(s)
# print(l)

# from collections import Counter

# dic1=[{'item':'item1','amount':400},
#       {'item':'item2','amount':300},
#       {'item':'item1','amount':750}] 

# to=Counter()

# for i  in dic1:
#     to[i["item"]]+=i['amount']

# print(to)
# import heapq

# dic1={'a':10,'b':20,'c':30,'d':10,'e':20}

# re=heapq.nlargest(3,dic1.values())

# print(re)

# str1='w3resource'

# co={}

# for i in str1:
#     if i in co:
#         co[i]+=1
#     else:
#         co[i]=1
# print(co)

# def ch(list1,sub):
#     res=False
#     for i in range(len(list1)):
#         if list1[i:i+len(sub)]==sub:
#             res=True
#     return res
       
# list1=[1,2,3,4,5,6,7]
# sub=[4,5,6]

# print(ch(list1,sub))

# tup_list=[(1,2,3),(4,5,6),(7,8,9)]

# n=[i[:-1]+(10,) for i  in tup_list]
# print(n)

















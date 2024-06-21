# Write a Python program to find the highest 3 values in a dictionary 

import heapq

dic1={'a':10,'b':20,'c':30,'d':400,'e':50}

h=heapq.nlargest(3,dic1.values())

print(h)

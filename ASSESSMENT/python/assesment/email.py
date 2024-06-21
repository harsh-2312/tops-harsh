 
import re

# email=input("enter email:")
# chak=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email)

# print(chak)


email=input("enter email:")
chak=re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email)

print(chak.group())
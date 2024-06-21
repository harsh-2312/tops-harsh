# Write a Python function to check whether a number is perfect or not.  



list1=[]
def per(num):
    for i in range(1,num+1):
        if num %i==0:
            list1.append(i)
    li=list1[:-1]
    if sum(li)==num:
        print(f"{num} is parfect number") 
    else:
        print("number is not parfect")
   
num=int(input("enter a num:"))
per(num)


        




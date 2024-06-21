#  Write a Python program to test whether a passed letter is a vowel or not. 
while(1):
    character=(input("enter character:")).lower()
    
    if character== 'a' or character=='e' or character=='i' or character=='o' or character== 'u':
        print("character is vowle--")
    else:
        print("consonants--")   
    choice=input("do you want check again(y/n):").lower()  
    if(choice!='y'):
       break     
print("thank you")
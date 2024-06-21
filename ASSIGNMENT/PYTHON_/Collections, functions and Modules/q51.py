#  Write a Python function that checks whether a passed string is palindrome or not


def palindrome(st1):
    rev=st1[::-1]
    if rev==st1:
        print(f'{st1} is palindrome')
    else:
        print(f'{st1} is not palinderome')


st1=input("enter string:")
palindrome(st1)



  
  
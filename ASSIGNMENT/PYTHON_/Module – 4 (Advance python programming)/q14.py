#  How many except statements can a try-except block have? Name Some 
# built-in exception classes:  

# -> ZeroDivisionError
# -> ValueError
# -> TypeError
# -> IndexError
# -> FileNotFoundError
# -> NameError


try:
    # x = 10/0
    num = int(input("Enter Number: "))
except ZeroDivisionError:
    print('Error: Division by zero')
except ValueError:
    print('Error: Invalid Value')
except Exception :
    print('somthig was wrong',Exception)
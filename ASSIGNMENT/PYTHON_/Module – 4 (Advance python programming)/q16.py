# Can one block of except statements handle multiple exception?  

try:
    res= 10 /0
    
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

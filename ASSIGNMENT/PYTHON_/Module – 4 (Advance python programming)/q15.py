#  When will the else part of try-except-else be executed? 

try:
    num= int(input("Enter number:"))
    res= 10 /num
    
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print(f"Division successful, result is {res}")

# When is the finally block executed?  

# >> The finally block will always be executed, no matter if the try block raises an error or not

try:
  x > 3
except:
  print("Something went wrong")
finally:
  print("The try...except block is finished")

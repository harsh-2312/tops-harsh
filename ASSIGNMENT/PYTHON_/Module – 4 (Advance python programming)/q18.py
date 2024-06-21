# What happens when „1‟== 1 is executed?  


print("1" == 1)  # This will output: False


# Python does not perform implicit type conversion between strings and integers when using the == operator.
# It compares both the type and the value, and since a string is not equal to an integer, the result is False.
#  How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets.  

def div_(y): 
    try: 
       
        res = 10/ y 
    except ZeroDivisionError: 
        print(" dividing by zero ") 
    else:
        print("res:", res) 
    finally:  
 
        print('This is always executed')   
 
div_(2) 
div_(0)
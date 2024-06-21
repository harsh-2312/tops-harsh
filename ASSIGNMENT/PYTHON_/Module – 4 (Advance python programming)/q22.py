# How to Define a Class in Python? What Is Self? Give An Example Of 
# A Python Class  


# >> you must create a class that will define the object with the "init()" constructor.

# >> The self is used to represent the instance of the class.



class student:
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def display(self):
        return self.n,self.a
    
obj=student('harsh',21)

print(obj.display())



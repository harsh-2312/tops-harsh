#  What is Instantiation in terms of OOP terminology?  

# >> Instantiation is a process of creating an instance of class

class person:
    def __init__(self,name):
        self.name = name
    
person1 = person('roy')
print(person1.name)
person2 = person('joy')
print(person2.name)
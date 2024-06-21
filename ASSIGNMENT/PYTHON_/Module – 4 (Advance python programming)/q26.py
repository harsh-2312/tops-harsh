# # Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python? 

# >> Constructors in Python is a special class method for creating and initializing an object instance at that class.


# single inheritance
class Parent:
    def func1(self):
        print("This is parent class.")
 
 
class Child(Parent):
    def func2(self):
        print("This is child class.")
 
object = Child()
object.func1()
object.func2()


# multiple inheritance
 
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


# Hierarchical inheritance
class Parent:
    def func1(self):
        print("This is parent class.")
 
class Child1(Parent):
    def func2(self):
        print("This is child 1.")
 
class Child2(Parent):
    def func3(self):
        print("This is child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Multilevel Inheritance
class Base:

    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role
 

class Intermediate(Base):
 
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age
 

class Derived(Intermediate):
  
    def __init__(self, age, name, roll, role):
        super().__init__(age, name, roll, role)
 
    def Print_Data(self):
        print(f"The Name is : {self.name}")
        print(f"The Age is : {self.age}")
        print(f"The role is : {self.role}")
        print(f"The Roll is : {self.roll}")
 

obj = Derived(21, "harsh", 25, "student")
obj.Print_Data()

# hybrid inheritance
 
class School:
    def func1(self):
        print("This is school.")
 
class Student1(School):
    def func2(self):
        print("This is student 1. ")
 
class Student2(School):
    def func3(self):
        print("This is student 2.")
 
class Student3(Student1, School):
    def func4(self):
        print("This is student 3.")
 
object = Student3()
object.func1()
object.func2()
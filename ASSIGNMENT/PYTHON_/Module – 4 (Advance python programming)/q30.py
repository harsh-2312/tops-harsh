# What relationship is appropriate for Student and Person? 

class student:
    def __init__(self,name ,id,age):
        self.name=name
        self.id=id
        self.age=age

    
class person(student):
    def __init__(self,name,age):
        self.name=name
        self.age=age

stu=student('RAJ',221,23)
per=person("tej",34)

print(stu.name,stu.age,stu.id)
print(per.name,per.age)



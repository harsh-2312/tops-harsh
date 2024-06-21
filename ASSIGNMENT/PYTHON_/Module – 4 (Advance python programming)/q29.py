# What relationship is appropriate for Course and Faculty?  



class Faculty:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, c_name):
        self.name = c_name
      

f = Faculty("hitesh")
cou= Course("Mathematics")

print(f.name)       
print(cou.name) 
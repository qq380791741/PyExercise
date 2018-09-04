class Student(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        return
    def print_student(self):
        print(self.name+str(self.age)+self.sex)
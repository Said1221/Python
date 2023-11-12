from datetime import date

class Student:
    def __init__(self , name , age , courses):
        self.name = name
        self.age = age
        self.__courses = courses  # ===> courses is private

    #instead method
    def describe(self):
        print(f"my name is {self.name} {self.age} years old and I study {self.__courses}")

    def is_old(self , age):
        if self.age >= age:
            print("is old")
        else:
            print("still young")

    def get_name(self):
        return self.name

    def set_name(self , newName):
        self.name = newName

    def birth(self , birthDay):
        self.age = date.today().year - birthDay

    #static method
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def add5(num):
        return num+5

    @staticmethod
    def add10(num):
        return num+10

    @staticmethod
    def PI(x,y):
        return 3.14

student1 = Student("Said" , 23 , ["python" , "Flutter"])
student2 = Student("Mohamed" , 24 , ["python" , "C++"])
student3 = Student("Ahmed" , 21 , ["python" , "C#"])

print(student1.name)
student2.describe()
student1.is_old(24)             # ===> compair student1 (23) >= 24 ??

print(student3.get_name())
student3.set_name("Mostafa")
print(student3.get_name())

student1.birth(2000)
student1.describe()

x = Student.add(5,10)
y = Student.add5(x)
z = Student.add10(y)
print(x,y,z)

class Person:
    def __int__(self , name , age):
        self.name = name
        self.age = age

    def display(self):
        return f"my name is {self.name} and I am {self.age}"


class Man(Person):
    def __init__(self , name , age , address):
        super().__init__(name,age)
        self.address = address


    def display(self):
        string = super().display()
        return string + f" and I am living in {self.address}"


man = Man("Said" , 23 , "Alex")
print(man.display())
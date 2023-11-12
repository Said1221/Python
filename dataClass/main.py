from dataclasses import dataclass

@dataclass
class person():
    name:str = "said"
    age:int = 23

ahmed = person("ahmed" , 22)
ibrahim = person("ibrahim" , 25)
print(ahmed == ibrahim)
print(ahmed.age , ibrahim.age)

#######################################

'Dunder methods'

class Order:
    def __init__(self , name , courses):
        self.name = name
        self.courses = courses

    def __len__(self):
        return len(self.courses)

    def __str__(self):
        return f"{self.name} study {self.courses}"

    def __bool__(self):
        return len(self.courses) > 2

    def __add__(self, other):
         self.courses.append(other)
         return self

    def __iadd__(self, other):                  # is same like +=
         self.courses.append(other)
         return self

    def __getitem__(self, item):
        return self.courses[item]

    def __setitem__(self, key, value):
        self.courses[key] = value
        return self


order = Order("said" , ["HTML" , "Python" , "CSS"])

print(len(order))

print(order)

print(bool(order))

order = order + "Flutter"
print(order.courses)

order += "Dart"
print(order.courses)

print(order[1])

order[1] = "Java"
print(order[1])

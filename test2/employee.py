class Employee:
    """Initial function"""
    def __init__(self , name , age , department):
        self.name = name
        self.age = age
        self.department = department

    def over(self):
        if self.age>=23:
            return "over"
        else:
            return "still UA"


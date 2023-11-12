def sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(sum(1,2,3,4))

################################

def my_sum(*args , option=True):
    result = 0
    if option:
        for x in args:
            result += x
        return result
    else:
        return result

print(my_sum(1,2,3,4 , option=False))

################################

def con(**kwargs):
    result = ""
    for x in kwargs.values():              # because i need the values of a , b and c
        result += x
    return result

print(con(a="said " , b="emad " , c="said"))


def human(**kwarge):
    for key , value in kwarge.items():     # because i need the values and the keys
        print(f"{key} : {value}")

human(name="said" , job="developer" , age=23)

################################

def show(x , y , *args , option=True , **kwargs):
    print(x,y)
    print(args)
    print(option)
    print(kwargs)

show(1 , 2 ,3 , 4 , option=False , say="hello " , somthing="world")

################################


list_of_char = [*"said emad said"]
print(list_of_char)
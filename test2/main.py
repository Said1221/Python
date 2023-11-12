from math import *
from  employee import Employee
from  details import  Detailes


# age = input("please enter your age : ")
# print("the age " + str(age))
#
# x = input("enter the first num : ")
# y = input("enter the second num : ")
# result = int(x) + int(y)
# print(result)

#########################################

# list = ["mohamed" , "said" , 12]
# print(list[0])

#########################################

# touble = (2 , 3)
# print(touble[1])

#########################################

# touble_in_list = [(2,3) , (4,5) , (6,7)]
# print(touble_in_list)
# print(touble_in_list[0])
# print(touble_in_list[0][1])

#########################################

# def name(name , x , y):
#     print("hello "+name)
#     return x*y
#
# print(name("said" , 2 , 6))

#########################################

# x = input("enter your number in the family : ")
#
# if int(x) == 1 or int(x) == 2:
#     print("hello Baba & Mama")
# elif int(x) == 3:
#     print("hello Nouran")
# elif int(x) == 4:
#     print("hello Said")

#########################################

# def getMax(x,y,z):
#     if x>=y and x>=z:
#         return x
#     elif y>=x and y>=z:
#         return y
#     else:
#         return z
#
# print(getMax(5,1,6))

#########################################

# months = {
#     "jan" : "january",
#     "feb" : "febraury"
# }
#
# print(months["feb"])

#########################################

# i = 0
# while i <=5 :
#     i += 1
#     if i==3 :
#         continue
#     print(i)

#########################################

# for letter in "said":
#     print(letter)
#
# names = ["mohamed" , "ahmed" , "said"]
# for x in names:
#     print(x)
#
#
# names = ["mohamed" , "ahmed" , "said" , "ibrahim" , "mostafa"]
# for x in range(len(names)):
#     if x % 2 == 0:
#         print(x, "is even")
#     else:
#         print(x, "is odd")

#########################################

#numList = [1,2,5,2,3,6,3,3,1,8,4,4,8,8,9,2,9]
# unique_list = []

# for num in numList:
#     if num not in unique_list:
#         unique_list.append(num)
#
# print(unique_list)

#unique_list = set(numList)
#print(unique_list)
#unique_list = list(unique_list)
#unique_list.append(5)
#print(unique_list)

#########################################

#def power(baseNum , powNum):
#    result = 1
#    for index in range(powNum):
#        result *= baseNum
#    return (result)

#print(power(3,3))

#########################################

'2D Lists & Nested Loops'

#list = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#]

#for row in list:
#    for column in row:
#        print(column)

#print(list[2])
#print(list[2][1])


#########################################

#try:
#    value = int(input('Enter Number : '))
#    print(value)
#except:
#    print('Invalid Number')

#########################################

'Reading Files'

#family = open('family' , 'r')

'is file able to read T/F'
#print(family.readable())

'read the file'
#print(family.read())

'read line by line'
#print(family.readline())

'read all and print it as a list'
#print(family.readlines())
#print(family.readlines()[2])

#family.close()

#########################################

#family = open('family' , 'a+')

#family.write("\nmy name is said")

#family.close()

#########################################

"""The Object"""

em1 = Employee("Mohamed" , 25 , "Facebook")
em2 = Employee("Said" , 23 , "PcLink")
em3 = Employee("Ahmed" , 22 , "Student")

print(em2.name , em2.age , " work in " ,em1.department )
print(em1.over())
print(em3.over())

det = Detailes()
det.address()
det.salary()
det.married()






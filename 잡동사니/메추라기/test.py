'''
j = int(input("1값"))
k = int(input("2값"))



if(j %2 == 0):
        j = j+1


for i in range(j, k+1,2):
        print(i, "  ")


'''

'''
def sum_mul(a, b):
    return (a+b), (a*b)

result = sum_mul(1,2)
print(type(result))
print (result)
'''
'''

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("aaaa", 27)
say_myself("aaaa", 27, True)
say_myself("aaaa", 27, False)
'''


'''
class User:
    phone = '  '
    email = ' '
    name = ' '
    def __init__(self, phone, email, name):
        self.phone = phone
        self.email = email
        self.name = name

    def init(self, p, e, n):
        self.phone = p
        self.email = e
        self.name = n

    def getphone(self):
        return self.phone

    def getemail(self):
        return self.email

    def getname(self):
        return self.name
        
        


    

user1 = User()
user1.init('010', 'lee' , 'sss')


print(user1.phone)
print(user1.email)
print(user1.name)



user2 = User('000', 'sss', 'ffa')

print(user2.phone)
print(user2.email)
print(user2.name)



users = []
users.append(user1)

print(users[0].getphone())
print(users[0].getemail())
print(users[0].getname())


user3 = {'phone' : '012', 'email' : 'ccc', 'name' : 'afc'}

print(user3['phone'])
print(user3['email'])
print(user3['name'])

'''

'''
class Employee:
    name = ""

    def __init__(self,name):
        self.name = name

    def working(self):
        print("%s가 일하고있다" %self.name)

    def go(self, where):
        print("%s가 %s에 가고있따" %(self.name,where))
        
    

emp1 = Employee("길동s")
emp1.working()
emp1.go("home")


'''


'''

class animal:
    def speak(self):
        print("animal Speaking")

    def eat(self):
        print("nyamnyam")

ani = animal()
ani.speak()


class dog(animal):
    def speak(self):
        print("walwal")


d = dog()
d.speak()
d.eat()
'''

'''
class A:
    def a(self):
        print("sss")


class Database:
    def open(self):
        print("database open")

class Oracle(Database):
    def select(self):
        print("oracle select")


class SqlServer(Database, A):
    def select_sql(self):
        print("sql select")





db2 = SqlServer()
db2.open()
db2.select_sql()
db2.a()
'''

'''

class Point:
    def __init__(self, x= 0, y=0):
        self.x = x
        self.y = y
    def __add__(self, point_v):
        return Point(self.x + point_v.x, self.y + point_v.y)

    def msg(self):
        print("x: %d, y: %d" %(self.x, self.y))


p = Point(1,2)
p1 = Point(2,3)
p2 = p + p1

p3 = p.__add__(p1)

p.msg()
p1.msg()
p2.msg()
p3.msg()
'''





'''
def add(a,b):
    return a+ b

def sub(a,b):
    return a- b

def mul(a,b):
    return a* b

def div(a,b):
    return a/ b


print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))

''''''

#c:\python37/cal.py


import cal
print(cal.add(1,2))
print(cal.sub(1,2))
print(cal.mul(1,2))
print(cal.div(1,2))




'''

from calculator.calculate.add import *


print(add(2,3))















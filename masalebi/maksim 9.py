class intset (object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove (self, e) :
        try:
            self.vals.remove(e)
        except:
            raise ValueError (str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        return '{'+','.join([str(e) for e in self.vals]) + '}'

def intersect(self, other):
    commonValueSet = intset()
    for val in self.vals:
        if other.member(val):
            commonValueSet.insert(val)
    return commonValueSet

def __len__(self):
    return len(self.vals)


list1 = intset()
print (list1)
list1.insert (3)
list1.insert (5)
list1.insert (36)
list1.insert (33)
list1. insert (25)
list1.insert(8)
print (list1)
print (list1.member (3))
list1. remove (33)
print (list1)
list2 = intset()
list2.insert(3)
list2.insert (33)
list2.insert (25)
list2.insert (998)
list2.insert(85)
print (list2)


class Animal (object) :
    def __init__(self, age) :
        self.age = age
        self.name = None
    def get_age (self) :
        return self.age
    def get_name (self) :
        return self.name
    def set_age (self, newage) :
        self.age = newage
    def set_name (self, newname="") :
        self. name = newname
    def __str__(self) :
        return "animal:"+str (self.name) +":"+str(self.age)

class Rabbit (Animal):
    tag = 1
    def __init__ (self, age, parent1=None, parent2=None) :
        Animal._init(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid (self) :
        return str(self.rid).zfill (3)
    def get_parent1 (self) :
        return self.parent1
    def get_parent2 (self) :
        return self.parent2


class Robot:
    def action(self):
        print('Robot action')
class HelloRobot(Robot):
    def action(self):
        print('Hello world')
class DummyRobot(Robot):
    def start(self):
        print('Started.')
r = HelloRobot()
d = DummyRobot()
r.action()
d.action()

class Human:
    def sayHello(self, name=None) :
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello mr. X')
# Create instance
obj = Human()
# Call the method
obj.sayHello()
#Call the method with a parameter
obj.sayHello('Guido')
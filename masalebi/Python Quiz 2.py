class Lists():
    def __init__(self,list1):
        self.list1 = list1
        print(self.list1)
    def counter(self):
        self.sum=sum(self.list1)
        self.minimum=min(self.list1)
        self.maximum=max(self.list1)
    def __str__(self):
        return "the sum : " + str(self.sum)+ "  the minimum : " + str(self.minimum) + "  the maximum : " + str(self.maximum)
list1= Lists([2,3,1,3,4,5,6,7,2,3,9,12,10])
list1.counter()
print(list1)


import random as r
def dicto(dic):
    for i in dic:
        if i == "a":
            dic[i].append(r.randint(1,10))
        elif i == "b":
            dic[i].append(r.randint(1,10))
        elif i == "c":
            dic[i]+=[r.randint(1,10)for i in range (4)]
        elif i == "d":
            dic[i]+=[r.randint(1,10) for i in range (7)]

    max = 0
    ans = None
    mult=1
    for key, value in dic.items():
        curr = len(value)
        if curr > max:
            max = curr
            ans = key
        for i in value:
            mult*=i
    return ans,mult

a={'a': [], 'b': [], 'c': [], 'd': []}
print(dicto(a))


def hello(s):
    b = 0
    for i in range (len(s)):
        if s[i:i+5] == 'hello':
            b+=1
    return b
s = 'hihellohellonohellon'
print(hello(s))


def decbin(a):
    result=''
    while a>0:
        result+=str(a%2)
        a=a//2
    return result
print(decbin(45))


def bindec(a):
    for i in a:
        if i != '0' and i != '1':
            raise ValueError("You need to input only binary number, so only 0 or 1 ")
    b=len(a)-1
    c=0
    for i in a:
        if i=='1':
            c+=2**b
        b-=1
    return c
try:
    print(bindec('101101'))
except ValueError as e:
    print(e)
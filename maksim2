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
def dicto(dico):
    for i in dico:
        if i == "a":
            dico[i].append(r.randint(1,6))
        elif i == "b":
            dico[i].append(r.randint(1,6))
        elif i == "c":
            count=0
            while count<4:
                dico[i].append(r.randint(1,6))
                count+=1
        elif i == "d":
            count1=0
            while count1<7:
                dico[i].append(r.randint(1,6))
                count1+=1
    mult=1
    max=0
    ans=None
    for i,j in dico.items():
        curr=len(j)
        if curr>max:
            max=curr
            ans=i
        for i in j:
            mult*=i
    return dico,ans,mult

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

def rows(a):
    b=''
    for i in range (a):
        b+=(chr(ord('B')+i))
        print(b)
rows(6)


def longtask():
    num = r.randint(1,10)
    print("our number is : ",num)
    if num == 1:
        words = []
        for i in range(8):
            word = input("Enter a word: ")
            words.append(word)
        for i in words:
            if len(i)>1:
                print("Second letters of a word: ",i[1])

    elif num == 2:
        items = []
        for i in range(10):
            numb = int(input("Enter an item: "))
            items.append(numb)
        items2 = [item for item in items if item % 2 != 0]
        print("List without even numbers : ", items2)

    elif num == 4:
        dic = {}
        for i in range(6):
            key = input("Enter a key: ")
            value = input("Enter a value: ")
            dic[key] = value
        tup=()
        for i in dic.keys():
            tup+=((i,dic[i]),)
        print("Dictionary items as tuples: ", tup)

    elif num == 5:
        text = input("Enter text: ")
        words = text.split()
        print("Text as a list of words: ", words)

print(longtask())



def shekvetis_gaketeba(shekveta):
    products = ["xachapuri", "xinkali", "mcvadi", "kababi", "salata"]
    counts = {i: 0 for i in products}
    items = shekveta.split()
    for i in items:
        if i in products:
            counts[i] += 1

    result = ""
    for i in products:
        count = counts[i]
        if result != "":
            result += " "
        result += i + ": " + str(count)

    return result
shekveta = "xachapuri xinkali xachapuri kababi salata mcvadi salata salata"
print(shekvetis_gaketeba(shekveta))



import random
a = set()
for i in range(50):
    a.add(random.randint(1, 100))
jami = sum(a)
tup = ()
for i in a:
    tup += (i,)
listo = [i for i in a]
print("Set:", a)
print("Sum of elements:", jami)
print("Tuple:", tup)
print("List:", listo)



import random as r
def tupalo(tup):
    for i in range(0, 100):
        tup += (r.randint(0, 100),)
    tup2,tup3,tup4=(),(),()
    for i in tup:
        if i%2==0:
            tup2+=(i,)
        elif i%3==0:
            tup3+=(i,)
        else:
            tup4+=(i,)
    print(tup2,tup3,tup4)
    a = open('lukas.txt', 'w')
    a.write(str(tup2) + '\n')
    a.write(str(tup3) + '\n')
    a.write(str(tup4) + '\n')
    a.close()

tup=()
print(tupalo(tup))


def string(a):
    now=a[0]
    best=''
    for i in range(len(a)):
        if len(now)>len(best):
            best=now
        if a[i]>=a[i-1] and a[i-1]!='a':
            now+=a[i]
        else:
            now=a[i]
    return best
print(string("yzabbdecw"))



def tupli(a):
    b=()
    for i in a:
        if 'a' in i and 'e' in i and i.startswith('m'):
            b+=(i,)
    return b
a=('hello','friend','you', 'are','maestro','great','teacher','master','money','machu')
print(tupli(a))


def fibit(a):
    b,c=0,1
    count=0
    while c!=a:
        b,c=c,b+c
        count+=1
    return count
print (fibit(8))


class Tuple():
    def __init__(self):
        self.elements = ()

    def add(self):
        for i in range(0, 5):
            self.elements = (self.elements) + (random.randint(0, 10),)

    def remove(self, number):
        new = ()
        if number not in self.elements:
            raise Exception("Element is not present in Tuple")
        else:
            for i in self.elements:
                if i != number:
                    new += i,

        self.elements = new

    def __add__(self, other):
        new = ()
        for i in range(len(self.elements)):
            new = new + (self.elements[i] + other.elements[i],)
        return new

    def mutual(self, other):
        tupa = ()
        for i in self.elements:
            if i in other.elements:
                tupa += (i,)
        return tupa

    def __str__(self):
        return "result : " + str(self.elements)


bruh = Tuple()
bruh.add()
print(bruh)
brev = Tuple()
brev.add()
print(brev)
print(bruh + brev)
print(bruh.mutual(brev))



a=set()
a.add(5)
a.update([5,6,7,8,9])
a.remove(5)
a.discard(8)
a.pop()
a.clear()

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)
print(a&b)
print(a-b)

a=[5,6,3,2,5,6]
print(len(a))
print(len(set(a)))
if len(a)>len(set(a)):
    print("oo duplicates")
else:
    print("no duplicates")



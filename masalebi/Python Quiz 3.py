def rows(a):
    b=''
    for i in range (a):
        b+=(chr(ord('B')+i))
        print(b)
rows(6)


import random as r
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



class Tuple():
    def __init__(self, x):
        self.x = x
        print(self.x)
    def counter(self):
        self.sum=sum(self.x)
        self.minimum=min(self.x)
        self.maximum=max(self.x)
    def even(self):
        tup2=()
        for i in self.x:
            if i % 2 == 0:
                tup2+=(i,)
        return tup2
    def __str__(self):
        return "minimum : " +  str(self.minimum) +  "  maximum : " + str(self.maximum)

tup=Tuple((3,4,5,6,7,4,3,3))
tup.counter()
tup.even()
print(tup)
print(tup.even())



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


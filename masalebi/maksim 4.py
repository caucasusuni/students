def fibrec(a):
    if a<=1:
        return 1
    else:
        return fibrec(a-1) + fibrec(a-2)
print(fibrec(int(input("please enter a number: "))))

import module
a=500
b=800
print(a)
print(module.a)
module.hi()

import circle
pi = 3
print(pi)
print(circle.pi)
print(circle.area((3)))
print(circle.circumference(3))

a=open("lukas.txt","w")
for i in range(5):
    a.write(input("enter a word: ")+"\n")
a.close()

L=(5,6,7,2)
L=L+(100,)
print(L)
L=5
J=8
L,J=J,L
print(L)
def helo():
    return 5+7,5-7
L,J=hi()
print(L)

import random
T=()
for i in range(20):
    T=T+(random.randint(0,100),)
print(T)

a=((5,"str"),(8,"str"),(10,"papito"))
def aTuple(a):
    b, c = (), ()
    for i in a:
        b += i[0],
        if i[1] not in c :
            c+=i[1],
    return b,c,len(b),len(c)
print(aTuple(a))

a=('i','am','a','test','tuple')
def oddTuples(a):
    b=()
    for i in range(len(a)):
        if i%2==0:
            b+=a[i],
    return b
print(oddTuples(a))
import random as r
def listo(a):
    b,c=[],[]
    for i in range(len(a)):
        if a[i]%2==1:
            b.append(a[i])
        if i%2==1:
            c.append(a[i])
    d=sum(a)
    return a,b,c,d
a=[r.randint(0,100) for i in range(5)]
print(listo(a))

def applytoeach(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])
    return L
print(applytoeach([5,6.2,-8,9.2],abs))

def applytoeach2(L,x):
    for f in L:
        print(f(x))
applytoeach2([int,abs],-5.2)

for i in map(abs,[5,6.2,-8,9.2]):
    print (i)

L1=[1,5,3]
L2=[2,4,5]
for i in map(min,L1,L2):
    print(i)

def applytoeach3(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])
    return L
def fun(n):
    return n*5
print(applytoeach3([1,-4,8,-9],fun))

name=['John','Smith','Denise','Katy']
grade=['B','A+','A','A']
course=[2.00,6.0001,20.002,9.01]
def names(n,g,c):
    i=n.index(pop)
    return g[i]+" "+str(c[i])
pop=input("please enter a name: ")
print(names(pop,grade,course))

def count_names(names):
    dict = {}
    for i in names:
        dict[i] = names.count(i)
    return dict
N = ['nika', 'nika', 'nika', 'mari', 'mari', 'gigi']
print(count_names(N))

def count_names2(names):
    myDict={}
    for i in names:
        if i in myDict:
            myDict[i]+=1
        else:
            myDict[i]=1
    return myDict
print(count_names2(N))


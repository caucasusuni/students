a="101101"
b=0
for i in range(len(a)):
    b+=int(a[i])*(2**((len(a)-1)-i))
print(b)

c=19
d=[]
while c!=0:
    if c/2==c//2:
        d.append("0")
    else:
        d.append("1")
    c=c//2
print(d[::-1])

num1=19
result=""
while num1>0:
    result=str(num1%2)+result
    num1=num1//2
print(result)

x=0.375
p=0
while x*2**p%1 !=0:
    p+=1
print(p)
num=x*2**p
print("num=",num)
num=bin(int(num))
num=num[2:]
print(num)
for i in range (p-len(num)):
    num="0"+num
print(num)
num="0."+num
print(num)

epsilon=0.01
y=24000.0
guess=y/2.0
num_guesses=0

while abs(guess*guess - y) >= epsilon:
    num_guesses=num_guesses+1
    guess=guess - (((guess**2)-y)/(2*guess))
print(num_guesses)
print(guess)

def f(y):
    x=1
    x+=1
    print(x)
x=5
f(x)
print(x)

def g(x):
    def h():
        x='abc'
        return x
    x=x+1
    print('in g(x): x =',x)
    h()
    return x
x=3
z=g(x)

def printname(name,secname,reverse):
    if reverse:
        print (secname,name)
    else:
        print (name,secname)
printname("John","doe",True)


def square(x):
    return (x**2)
def fourthPower(x):
    return square(square(x))
print(fourthPower(2))


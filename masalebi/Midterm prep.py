def findbob(a):
    b = 0
    for i in range (len(a)):
        if a[i:i+3] == 'bob':
            b+=1
    return b
a = 'bobobegghbob'
print(findbob(a))

def longstring(a):
    current = a[0]
    big = ""
    for i in range(1, len(a)):
        if len(current) > len(big):
            big = current
        if a[i] >= a[i - 1]:
            current += a[i]
        else:
            current = a[i]
    return big
a = 'azcbobobegghakl'
print(longstring(a))

def square(a):
    y = 1
    ans = a
    while a > y:
        ans += a
        y += 1
    return ans
print(square(4))

def bintodec(a):
    b = 0
    l=len(a)-1
    for i in a:
        if i == '1':
            b += 2**l
        l-=1
    return b
a="101101"
print(bintodec(a))

def tup(a):
    b=()
    for i in a:
        if "a" in i and "b" in i and len(i) > 4:
            b +=(i,)
    return b
a=('haha','boo','aballo','true','boats','georgia','to','europe','yees','here','we','come','finally','thanks','mamarda')
print(tup(a))

def hello(a):
    counter=0
    for i in range(len(a)):
        if a[i:i+5]=="hello":
            counter+=1
    return counter
a = "hihellohellonohellon"
print(hello(a))

import random as r
def gcd(a,b,c):
    d=min(b,c)
    if a == 1:
        while c>0:
            if b%d==0 and c%d==0:
                return d
            else:
                c-=1
    elif a == 0:
        if c==0:
            return b
        return gcd(a,c,b%c)
a=r.randint(0,1)
b,c=5,10
print(gcd(a,b,c))

def cube_root_bisectional(num, epsilon=0.00001):
    low = 1
    high = num
    guess = (low + high) / 2
    while abs(guess**3 - num) >= epsilon:
        if guess**3 < num:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess
number = 27
print("Cube root of", number, "is approximately:", cube_root_bisectional(number))

def cube_root_newton_raphson(num, epsilon=0.00001):
    if num == 0:
        return 0
    guess = num / 2
    while abs(guess**3 - num) >= epsilon:
        guess = guess - (guess**3 - num) / (3 * guess**2)
    return guess
number = 27
print("Cube root of", number, "is approximately:", cube_root_newton_raphson(number))

def recpow(a,b):
    if b==1:
        return a
    else :
        return a*recpow(a,b-1)
print(recpow(5,2))

def iterpow(a,b):
    c=1
    while b > 0 :
        c*=a
        b-=1
    return c
print(iterpow(5,3))

def dectobin(a):
    result=""
    while a>0:
        result=str(a%2)+result
        a=a//2
    return result
a=19
print(dectobin(a))

def pal(a):
    if len(a)<=1:
        return True
    else:
        return a[0]==a[-1] and pal(a[1:-1])
print(pal("opo"))

def fibit(a):
    b,c=1,1
    while a>1:
        b,c,a=c,b+c,a-1
    return c
print(fibit(5))

def big3(a):
    b=sorted(a,reverse=True)
    c=b[:3]
    ans=1
    for i in c:
        ans*=i
    return ans
a=[3,4,5,3,4,5,2]
print(big3(a))

def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
            break
    else:
        return True
print(prime(12))

def tuput(a):
    b,c,d=(),(),()
    for i in a:
        if i%2==0:
            b+=(i,)
        elif i%3==0:
            c+=(i,)
        else:
            d+=(i,)
    e=open("lukas.txt","w")
    e.write(str(b)+'\n')
    e.write(str(c)+'\n')
    e.write(str(d)+'\n')
    e.close()
    return b,c,d
a=()
for i in range(50):
    a+=(r.randint(0,100),)
print(tuput(a))

def testo(a):
    current=a[0]
    best=''
    for i in range(1,len(a)):
        if len(current)>len(best):
            best=current
        if a[i]>=a[i-1]:
            current+=a[i]
        else:
            current=a[i]
    return best
print(testo("abcdefghfht"))

def bruh(a,b,c):
    if a==1:
        d=min(b,c)
        while d>0:
            if b%d==0 and c%d==0:
                return d
            else:
                d-=1
    elif a==0:
        if c==0:
            return b
        else:
            return bruh(a,c,b%c)
a=r.randint(0,1)
b,c=15,12
print(bruh(a,b,c))



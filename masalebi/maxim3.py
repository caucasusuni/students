def foo(x,y=5):
    def bar(x):
        return x+1
    return bar(y*2)
print(foo(3))

def fool(x):
    def baro(z,x=0):
        return x+z
    return baro(3)
print(fool(5))

def mult(a,b):
    if b==1:
        return a
    else:
        return a+(mult(a,b-1))
print(mult(5,5))

def bruh(a,b):
    answer=0
    while b>0 :
        answer+=a
        b-=1
    return answer
print(bruh(5,7))

def fact(a):
    result=1
    for i in range(1,a+1):
        result*=i
    return result
print(fact(5))

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(5))

def iterpower(base,exp):
    answer=1
    while exp > 0:
        answer=answer*base
        exp-=1
    return answer
print(iterpower(5,3))

def recpower(base,exp):
    if exp == 0:
        return 1
    else:
        return base*recpower(base,exp-1)
print(recpower(5,3))

def printMove(fr,to):
    print('move from '+str(fr)+' to '+str(to))
def Towers (n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
print(Towers(4,'p1','p3','p2'))

def gcd(num1,num2):
    c=min(num1,num2)
    while c>0:
        if num1%c==0 and num2%c==0:
            return c
        else:
            c-=1
print(gcd(15,20))

def gcd1(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd1(124,16))

def gcdrecur(a,b):
    if b==0:
        return a
    else:
        return gcdrecur(b,a%b)
print(gcdrecur(124,16))


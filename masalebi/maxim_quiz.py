def binary_to_decimal(a):
    decimal = 0
    power = len(a) - 1
    for i in a:
        if i == '1':
            decimal += 2 ** power
        power -= 1
    return decimal
a="101101"
print(binary_to_decimal(a))

def tup(a):
    b=()
    for i in a:
        if "a" in i and "b" in i and len(i)>4:
            b+=(i,)
    return b
a=('haha','boo','aballo','true','boats','georgia','to','europe','yees','here','we','come','finally','thanks','mamarda')
print(tup(a))

import random as r
def fun(a):
    b,c,d=(),(),()
    for i in a:
        if i % 2 == 0:
            b += (i,)
        elif i % 3 == 0:
            c += (i,)
        else:
            d += (i,)
    f = open("lukas.txt", 'w')
    f.write("Even numbers: " + str(b) + '\n')
    f.write("Multiples of three: " + str(c) + '\n')
    f.write("Odd numbers: " + str(d) + '\n')
    f.close()
    return b, c, d
a=()
for i in range(50):
    a=a+(r.randint(0,100),)
print(fun(a))

def fibrec(a):
    if a<=1:
        return 1
    else:
        return fibrec(a-1) + fibrec(a-2)
answer=fibrec(int(input("please enter a number: ")))
f = open("lukas.txt", 'w')
f.write(str(answer))
f.close()

def randomer(a,num1,num2):
    if a == 0:
        result = 0
        for i in range(num1):
            result += num2
        return result
    elif a == 1:
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        return result
    else:
        if num1 == 0:
            return 0
        return num2 + randomer(a,num1 - 1, num2)
a = r.randint(0, 2)
num1 = r.randint(0, 10)
num2 = r.randint(0, 10)
print(randomer(a,num1,num2))
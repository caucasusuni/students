print(float("nan"))
a=5
b=0
try:
    print (a/b)
except ZeroDivisionError:
    raise ZeroDivisionError ("Divide by zero")
print ("morcha")

def funco(a,b):
    c=[]
    for i in range(len(a)):
        try:
            c.append(a[i]/float(b[i]))
        except ZeroDivisionError:
            c.append(float('nan'))
        except:
            raise ValueError ("Type Error")
    return c
a=[5,6,7,2,4]
b=[5,2,0,2,2]
print(funco(a,b))

def bub(a):
    b=[]
    for i in a:
        b.append([i[0],i[1],avg(i[1])])
    return b
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("No grades data")
        return 0.0

a=[[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]]]
print(bub(a))


def dido(a,index):
    denom=a[index]
    try:
        return [divi(item,denom)for item in a]
    except ZeroDivisionError:
        print("Divide by zero")
def divi(item,denom):
    return item/denom

a=[6,5,3,0,5]
index=3
print(dido(a,index))

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

def my_function(x):
    return list(dict.fromkeys(x))
mylist=my_function(["a","b","a","c","c"])
print(mylist)

a=[5,6,5,6,7,8]
b=[]
for i in range(len(a)):
    if a[i] not in a[i+1:]:
        b.append(a[i])
print(b)


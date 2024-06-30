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

def man(dict):
    tup = []
    count = 0
    for i in dict:
        if dict[i] > count:
            count += 1
        else:
            count = dict[i]
    for i in dict:
        if dict[i] == count:
            tup.append(i)
    return tup, count

D = {'nika': 1, 'mari': 2, 'gigi': 4, 'sopo': 4}
print(man(D))

def butt(dict):
    values=dict.values()
    best= max(values)
    words=[]
    for i in dict:
        if dict[i]==best:
            words.append(i)
    return words,best
D = {'nika': 1, 'mari': 3, 'gigi': 4, 'sopo': 4}
print(butt(D))


def wordo(dict,mino):
    result=[]
    done=False
    while not done:
        temp=butt(dict)
        if temp[1]>=mino:
            result.append(temp)
            for i in temp[0]:
                del dict[i]
        else:
            done=True
    return result
print(wordo(D,3))

animals = {'a':['aardvark'], 'b':['baboon'], 'c':['coati']}
animals['d']=['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def anomaly(animals):
    count=0
    for i,j in animals.items():
        for k in j:
            count+=1
    return count
print(anomaly(animals))

def anomaly(animals):
    return sum(len(j) for j in animals.values())
print(anomaly(animals))

def anomaly(animals):
    counter=0
    for i in animals:
        counter +=len(animals[i])
    return counter
print(anomaly(animals))

def biggo(animals):
    big=0
    collect=[]
    if len(animals)==0:
        return None
    for i in animals:
        if len(animals[i])>=big:
            big=len(animals[i])
            collect=i
    return collect
print(biggo(animals))

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n]=ans
        return ans
d={1:1,2:2}
print(fib_efficient(10,d))

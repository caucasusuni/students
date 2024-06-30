def isPal(x):
    assert type(x)==list
    temp=x[:]
    temp.reverse()
    if temp==x:
        return True
    else:
        return False

def silly(n):
    result=[]
    for i in range(n):
        elem=input("enter element : ")
        result.append(elem)
    if isPal(result):
        print("yes")
    else:
        print("no")
print(silly(5))

try:
    a=int(input("enter number : "))
    b=int(input("enter number : "))
    c=a/b
except ZeroDivisionError as e:
    print("no zeroo"+str(e))
except ValueError as e:
    print("invalid input"+str(e))
except:
    print("something went wrong")
else:
    print(c)
finally:
    print("finito")


while True:
    try:
        n = input("Enter a number: ")
        n = int(n)
        break
    except ValueError:
        print("Please enter a number")
print("correct input of an integer")

data=[]
file_name=input("Enter file name: ")
try:
    fh=open(file_name,'r')
except IOError:
    print("File cannot be opened")
else:
    for new in fh:
        if new !='\n':
            addIt=new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()
print(data)

data=[]
file_name=input("Enter file name: ")
try:
    fh=open(file_name,'r')
except IOError:
    print("File cannot be opened")
else:
    for new in fh:
        if new !='\n':
            addIt=new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()
print(data)

bruh=[]
if data:
    for student in data:
        try:
            name=student[0:-1]
            grades=int(student[-1])
            bruh.append([name,[grades]])
        except ValueError:
            bruh.append([student[:],[]])
print(bruh)
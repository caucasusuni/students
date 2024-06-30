s="hihellohellonohellon"
counter=0
for i in range(len(s)):
    if(s[i:i+5]=="hello"):
        counter+=1
print(counter)

a='abcdefghsdfh'
current=a[0]
big=""
for i in range(1,len(a)):
    if len(current)>len(big):
        big=current
    if a[i]>=a[i-1]:
        current+=a[i]
    else:
        current=a[i]
print(big)

num=int(input("enter number: "))
output=''
for i in range(num):
    output+=chr(ord('a')+i)
    print(output)
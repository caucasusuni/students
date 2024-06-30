a="azcbobobegghakl"
count=0
for i in range(len(a)):
    if(a[i:i+3]) =="bob":
        count+=1
print(count)

count1=0
for i in range(1,len(a)):
    if a[i]=="b" and a[i+1]=='o' and a[i+2]=="b":
        count1+=1
print(count1)

print(ord("a"))
print(chr(97))
print("b">"e")

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

x=3
y=1
ans=x
while x>y:
    ans+=x
    y+=1
print(ans)

b=int(input("Enter number: " ))
ans=0
while ans**3<abs(b):
    ans+=1
if ans**3!=abs(b):
    print("bruh")
else:
    if b<0:
        ans=-ans
print(ans)

for ans in range(b + 1):
    if ans ** 3 ==b:
        print(ans)

epsilon=0.01
guess=0.0
increment=0.0001
num_guesses=0
while abs(guess**3-b)>=epsilon:
    guess+=increment
    num_guesses+=1
print(num_guesses,guess)

low=1.0
high=b
ans=((high + low) / 2)
while abs(ans**2-b)>=epsilon:
    num_guesses+=1
    if ans**2 > b:
        high=ans
    else:
        low=ans
    ans=((high + low) / 2)
print(num_guesses,ans)
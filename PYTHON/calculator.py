a1=int(input())
a2=int(input())
a3=input()
b=a1+a2
c=a1-a2
d=a1/a2
e=a1*a2
if a3=="+":
    print(b)
elif a3=="-":
    print(c)
elif a3=="/":
    print(d)
elif a3=="*":
    print(e)
else:
    print("invalid operation")
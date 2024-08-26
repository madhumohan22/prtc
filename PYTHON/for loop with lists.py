a=[]
print("ji:")
for i in range(5):
    num=int(input("input"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)
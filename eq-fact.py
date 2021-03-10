n=int(input("enter the no"))
f=1
s=1
for i in range(1,n+1):
    f=f*i
    if(i>1 and i%2!=0):
        s=s+(i/f)
print("sum=",s)

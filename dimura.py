n=[]
for x in range(1000,2001,1):
     if(x%7==0) and (x%5==0):
         n.append(str(x))
print("the numbers are:",n)

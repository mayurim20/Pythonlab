def factors(x):
    print("the factors of",x,"are :")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
num=int(input("enter the no:"))
factors(num)
            
output:
    enter the no:432
the factors of 432 are :
1
2
3
4
6
8
9
12
16
18
24
27
36
48
54
72
108
144
216
432

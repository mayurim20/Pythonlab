def armstrong(l,h):
   for num in range(l,h+1):
      sum=0
      temp=num
      while temp>0:
          digit=temp%10
          sum=sum+(digit**3)
          temp//=10
      if(num==sum):
          print(num)
a=int(input("enter the lower limit"))
b=int(input("enter the upper limit"))
armstrong(a,b)
          













            
 
  

n=int(input("enter number"))
cnt=0
i=1
while(i<=n):
     if(n%i==0):
      cnt=cnt+1
     i+=1
if(cnt==2):
     print("prime")
else:
     print("not prime")

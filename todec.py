p=int(input())
l=str(p)
sum=0
for i in range(0,len(l)):
    u=p%10
    v=2**i
    p=p//10
    z=u*v
    sum=sum+z
    
print(sum)

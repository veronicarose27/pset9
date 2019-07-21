k,l=map(int,input().split())
y=[(i,j) for i in range(k) for j in range(l) if i+j==(k/2) and i*j==l]
if len(y)>0:
    print("yes")
else:
    print("no")    

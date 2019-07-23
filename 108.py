p=int(input())
k=list(map(int,input().split()))
l=[]
sum=0
for i in range(0,p):
    sum=sum+k[i]
    l.append(sum)
print(*l)

p=int(input())
k=list(map(int,input().split()))
for i in range(0,p):
    if(i%2!=0):
        temp=k[i]
        k[i]=k[i-1]
        k[i-1]=temp
print(*k)

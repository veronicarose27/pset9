d=int(input())
k=list(map(int,input().split()))
p=sorted(k)
for i in k:
    if i in p:
        l=p.index(i)
        print(l+1,end=" ")

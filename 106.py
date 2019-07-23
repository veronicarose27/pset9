d=int(input())
k=list(map(int,input().split()))
p=[]
for i in k:
    if i not in p:
        p.append(i)
print(*p)

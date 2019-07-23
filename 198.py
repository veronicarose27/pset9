p=int(input())
l=list(map(int,input().split()))
k=max(l)
m=min(l)
y=l.index(k)
x=l.index(m)
j=y-x
print(j)

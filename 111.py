p,m=map(int,input().split())
l=p+m
e=[]
h=[]
q=list(map(int,input().split()))
for i in range(0,p):
    for j in range(p,l):
       if(q[i]==q[j]):
           e.append(q[i])
for k in e:
    if k not in h:
        h.append(k)
print(*h)

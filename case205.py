t=str(input())
k=list(t)
u=[]
for i in k:
    p=ord(i)
    if p in range(65,91):
        l=p+32
    else:
        l=p-32
    u.append(chr(l))
print("".join(u))

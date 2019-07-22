w=input()
l=list(w)
p=[]
for i in w:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        p.append(i)
        l.remove(i)
k=p+l
print("".join(k))

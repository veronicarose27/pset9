o,p=map(int,input().split())
o=str(o)
l=[]
for i in range(0,p+1):
    if str(i) not in o:
        print("no")
        break
else:
    print("yes")

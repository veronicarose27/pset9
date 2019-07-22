l,m=(map(str,input().split()))
if(l=='R' and m=='P') or (l=='P' and m=='R'):
    print("P")
elif(l=='R' and m=='S' or l=='S' and m=='R'):
    print("R")
elif(l=='S' and m=='P' or l=='P' and m=='S'):
    print("S")
elif(l==m):
    print("D")

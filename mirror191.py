p=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
if(m==l[::-1]):
    print("yes")
else:
    print("no")

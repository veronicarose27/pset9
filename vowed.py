l=['a','e','i','o','u','A','E','O','U','I']
h=[]
count=0
n=int(input())
for i in range(0,n):
    s=str(input())
    for i in s:
        if i in l:
            count=count+1
    h.append([s,count])
    count=0
h.sort(key=lambda x:x[1],reverse=True)
for i in range(0,n):
    print(h[i][0])

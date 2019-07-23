l=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
p=input()
k=p[::-1]
if(p==k):
    print("yes")
else:
    for i in l:
        x=p+i
        h=x[::-1]
        if(x==h):
            print("yes")
            break
    
    else:
        print("no")

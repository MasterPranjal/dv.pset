print("enter 5 numbers with a space between them")
items=input().split(' ')
M=[int(i) for i in items]

def descending(L):
    flag=0
    for i in range(1,5,1):
        if (L[i-1]<L[i]):
            flag=1
    if(flag==0):
        print("descending")
    else:
        print("none")

def ascending(L):
    flag=0
    for i in range(1,5,1):
        if(L[i-1]>L[i]):
            flag=1
    if(flag==0):
        print("ascending")
    elif(flag==1):
        (descending(L))

ascending(M)

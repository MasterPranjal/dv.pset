n=int(input("enter the upper limit"))

def is_divisable(N):
    count=0
    for i in range(1,N,1):
        if (i%7==0):
            count=count+1
    return count

print(is_divisable(n))

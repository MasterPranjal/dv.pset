def multiples():
    A=[]
    x=0
    for x in range (0,1000):
        if (x%3==0) or (x%5==0):
            A.append(x)
    print(A)
    for j in range (len(A)):
        a=a+A[j]
    print ('sum=', a)
print (multiples())

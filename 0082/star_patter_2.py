n=int(input("Input = "))

def starPattern(n):
    for i in range(0,n):
        i +=1
        print ("*" *(i+0))

    for j in range(-n,0):
        j +=1
        print ("*" *(-j+1))

    starpattern()

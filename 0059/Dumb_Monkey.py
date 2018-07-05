# monkey climbing

P = int(input("enter the length of the pillar = "))

def dumbMonkey(P):
    if (P < 3):
        print("monkey cannot climb")
    elif(P >= 3):
        if(P%2 == 0):
            print("monkey will fall,save him now....")
        else:
            print("Yes, finally monkey has finally climbed")

dumbMonkey(P)

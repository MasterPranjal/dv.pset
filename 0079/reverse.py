x = int(input("Please enter number which you want to reverse: "))

reverse = 0;

def reverseNumber(x):
    while(x>0):
        remainder = x%10
        reverse = (reverse*10)+remainder
        x = x//10

        print("Reverse of the entered number is = " reverse)
        

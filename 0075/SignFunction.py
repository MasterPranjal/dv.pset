#Write sign function: returns +1 or -1 based on the sign of argument passed.

num = int(input('Enter a number to check its sign is it (+ or -) = '))

def signFunction(num):
    if num < 0:
        print ("-1")
    else:
        print ("+1")

signFunction(num)

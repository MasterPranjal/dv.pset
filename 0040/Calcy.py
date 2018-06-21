def add(x,y):
    return x+y
def sub(a,b):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

z=input("Which operator do you want to choose? (/,*,+,-)")

x=int(input("Enter X "))
y=int(input("Enter Y "))

if z == "+":
    print (add(x,y))
    
if z == "-":
    print (sub(x,y))
    
if z == "*":
    print (mul(x,y))

if z == "/": 
    print (div(x,y))

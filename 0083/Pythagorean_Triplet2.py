lhs = 0 #lefthandside
rhs = 0 #righthandside

a = int(input('Enter a which is one of the side of a triangle (condition to be lept in mind a<b<c) = '))
b = int(input('Enter b = '))
c = int(input('Enter c = '))

def lefthandside():
    lhs=(a**2)+(b**2)
    return lhs

def righthandside():
    rhs=(c**2)
    return rhs

lhs = lefthandside()
rhs = righthandside()

if lhs == rhs:
    print ('True, the pythagoras theorem is prooved')
else:
    print ('The inputs does not form the Pythagorean triplet ')

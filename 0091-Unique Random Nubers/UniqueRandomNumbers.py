#Write a program that generates 5 unique random numbers.

import random
a = int(random.random()*1000)
b = int(random.random()*1000)
c = int(random.random()*1000)
d = int(random.random()*1000)
e = int(random.random()*1000)

def generateRandom(a,b,c,d,e):
    while (a!=b!=c!=d!=e):
        print (a,b,c,d,e)
        break

generateRandom(a,b,c,d,e)



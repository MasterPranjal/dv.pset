def lcm(x,y):
    return x * y 

n = 1
for i in range(1, 21):
     n = lcm(n, i)
print(n)

#Input: 12321

#digit sum = 1+2+3+2+1 = 9
#rverse sum = 1+2+3+2+1 = 9

n=int(input("Enter number:"))
t=n     #temporary
r=0     #reverse
d=0     #digitsum
rd=0    #reversedigit

def checkPalindrome(n)
    do:
        d = d + n % 10
        n = n / 10
    while(n!=0)     #calculating sum

    do:             #reverseing the number and calculating reverse sum 
       r = t % 10
       rd = rd * 10 + r
       t = t / 10
    while(t!=0)

    
if ( d == rd )
    print("Yes")
else:
    print("No")
           

     

# Write Indicator function: maps x to either 1 or 0, depending on
# whether or not x belongs to given set.

A = [2, 5, 6, 8, 9, 10]

x = int(input("Enter the number which belongs or does not belongs = "))

def indicator(A,x):
    j = 0
    while (j <= len(A)):
        if (x == A[j]):
            print("x = 1")
        else:
            print("x = 0")
    j = j+1 

indicator(A,x)

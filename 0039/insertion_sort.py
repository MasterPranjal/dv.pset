print("enter a number of items with space")
items=input().split(' ')
M=[int(i) for i in items]

def insertion_sort(L):
    for j in range(5):
        for i in range(5):
            if(L[i]>L[i+1]):
                k=L[i+1]
                L[i+1]=L[i]
                L[i]=k
    return L

print(insertion_sort(M))

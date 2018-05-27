
#Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
#           x = 180;
#Output : -1
#Element x is not present in arr[].

print("enter a number of items with space")
arr=input().split(' ')

x = int(input("enter item to search:"))

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

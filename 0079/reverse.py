#Practicing to reversing a number 

actual_num = int(input("Please enter number which you want to reverse = "))

global reverse

def reverseNumber(actual_num):
    reverse=0
    while(actual_num > 0):
        remainder = actual_num % 10
        reverse = (reverse*10) + remainder
        actual_num = actual_num // 10

    print("Reverse of the entered number is = ", reverse)

reverseNumber(actual_num)


        

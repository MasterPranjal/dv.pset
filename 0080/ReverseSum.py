'''
Write a function reverse_sum_and_check_equality(x)
which finds if the sum of digits of a number and sum of
digits of same number reversed will be same.

'''

actual_num = int(input("Please enter number which you want to reverse = "))

global reverse

def reverseNumber(actual_num):
    reverse=0
    while(actual_num > 0):
        remainder = actual_num % 10
        reverse = (reverse*10) + remainder
        actual_num = actual_num // 10
    return reverse

reverseNumber(actual_num)

def reverse_sum_and_check_equality(actual_num):
    sum = 0
    while(actual_num > 0):
        remainder = actual_num % 10
        sum = sum + remainder
        actual_num = actual_num // 10
    print(sum)

print("Sum of the digits of the actual number = ")
reverse_sum_and_check_equality(actual_num)

print("Sum of the reversed digits is = ")
reverse_sum_and_check_equality(reverseNumber(actual_num))
         

     

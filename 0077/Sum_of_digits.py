#Write a program that reads a number and display the sum of its digits.

number = int(input("Kindly enter the any number: "))

def Sum_of_digits(number):
    sum = 0
    while(number>0):
        remainder = number % 10
        sum += remainder
        number = number // 10
    return sum

sum = Sum_of_digits(number)

print("Sum of digitis ", sum)

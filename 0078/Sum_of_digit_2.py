#Write a function findSumOfDigits(x) which calculates the sum of its digits.
#Now write a computer program that reads two numbers and returns 1 if sum
#of their digits are equal and 0 otherwise.

number1 = int(input("Kindly enter the first number: "))

number2 = int(input("Kindly enter the second number: "))

def Sum_of_digits(number1):
    sum1 = 0
    while(number1 > 0):
        remainder = number1 % 10
        sum1 += remainder
        number1 = number1 // 10
    return sum1 

sum1 = Sum_of_digits(number1)

print("Sum of digitis of 1st number", sum1)

def Sum_of_digits(number2):
    sum2 = 0
    while(number2 > 0):
        remainder = number2 % 10
        sum2 += remainder
        number2 = number2 // 10
    return sum2 

sum2 = Sum_of_digits(number2)

print("Sum of digitis of 2nd number", sum2)

def comparison():
    if(sum1 == sum2):
        print(1)
    else:
        print(0)

comparison()

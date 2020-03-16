'''
@author: amayamunoz
'''
'''from builtins import True
from lib2to3.fixer_util import Number'''
'''from builtins import False'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract_two_numbers(num1, num2):
    differenceOfTwoNumbers = num2 - num1
    return differenceOfTwoNumbers

x = subtract_two_numbers(3, 4)

print(x)

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def problem_four_numbers(num1, num2, num3, num4):
    answerOfFourNumbers = num1 / num2 * num3 + num4
    return answerOfFourNumbers

x = problem_four_numbers(4, 2, 77, 10000)

print(x)

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def check_numbers(num1, num2):
    numbersEqual = num1 == num2
    numbersNotEqual = num1 < num2 or num1 > num2
    Number = num1 == num2
    if(numbersEqual):
        Number = True
    elif(numbersNotEqual):
        Number = False
    return Number

x = check_numbers(2, 2)
print(x)

x = check_numbers(3, 4)
print(x)

x = check_numbers(6, 3)
print(x)
    
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def numbers_take_in(num1, num2):
    largerNumber = num2 or num1
    equalNumbers = num1 == num2
    returnedNumber = num1 or num2
    
    if(largerNumber > num1 ):
        returnedNumber = num2
    elif(largerNumber > num2):
        returnedNumber = num1
    elif(equalNumbers):
        returnedNumber = num1
    return returnedNumber

x = numbers_take_in(2, 2)
print(x)

x = numbers_take_in(3, 2)
print(x)

x = numbers_take_in(4, 5)
print(x)

#5) Define a function that takes in two words and returns a string that contains both words combined.
def two_words(word1, word2):
    stringCombined = word1 + word2
    return stringCombined

x = two_words("Nice", "Hair")
print(x)
    
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def take_in_three_numbers(num1, num2, num3):
    numberEqual = num1 == num2 or num1 == num3
    returnedNumber = num1
    
    if(numberEqual == True):
        returnedNumber = True
    if(numberEqual == False):
        returnedNumber = False
    return returnedNumber

x = take_in_three_numbers(1, 2, 3)
print(x)

x = take_in_three_numbers(2, 2, 3)
print(x)

x = take_in_three_numbers(3, 2, 3)
print(x)
#7) Define a function that prints your name.
def my_name(word1, word2):
    myName = word1 + word2
    return myName

x = my_name("Margo", " Francour")
print(x)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def string_color_name(color1):
    myFavoriteColor = color1 == "Purple"
    
    if(myFavoriteColor == True):
        print("That's my favorite color!")
    elif(myFavoriteColor == False):
        print("That is not my favorite color. Try again.")
        
x = string_color_name("Purple")
print(x)

x = string_color_name("Blue")
print(x)
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def take_in_number(num1):
    numbersCompare = num1
    while(num1 > 0):
        print(numbersCompare)
        numbersCompare -= 1
        if(numbersCompare == 0):
            break
    return numbersCompare

x = take_in_number(5)
print(x)

#10) Create your own function that solves any problem you can think of.
def three_numbers(num1, num2, num3):
    productOfNumbers = num1 + num2 * num3
    return productOfNumbers

x = three_numbers(1, 2, 3)
print(x)

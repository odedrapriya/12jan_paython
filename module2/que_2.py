"""

Write a Python program to get the Factorial number of given number.

"""
num =int(input("Enter a number : "))
factorial = 1

if num < 0:
    print("factorial number dose not exist for Negative Number ")
elif num == 0:
    print("The factorial number of 0 is 1")
else:
    for i in range(1,num+1):
    factorial = factorial*i
print("The Factorial of",num,"is",factorial)
     
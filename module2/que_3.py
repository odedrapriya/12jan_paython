"""
Write a Python program to get the Fibonacci series of given range.

"""

num =int(input("Enter a number : "))
first = 0
second = 1
print(first)
print(second)
for x in range(1,num):
    third = first + second
    print(third)
    first,second=second,third

print(f'Fibonancci: {third}')

 
 

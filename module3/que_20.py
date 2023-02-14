"""
Write a Python program to replace last value of tuples in a list.
"""

list = [('p','r','y','a'),('o','d','e','d','r','a')]
print([t[:-1] + ('o') for t in list])
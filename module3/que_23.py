"""
Write a Python program to unzip a list of tuples into individual lists. 
"""

l = [(1,'priya'),(2,'sherya'),(3,'divya')]
print(list(zip(*l)))
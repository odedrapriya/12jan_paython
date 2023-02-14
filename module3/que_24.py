"""
Write a Python program to convert a list of tuples into a dictionary. 
"""

li = [(1,"priya"),(2,"Divya"),(3,"mahima"),(4,"vaishu")]
d = {}
for a,b in li:
    d.setdefault(a,[]).append(b)
print(d)
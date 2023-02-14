"""

Write a Python script to merge two Python dictionaries 
"""

dis1 = {1:'priya' , 2:'divya'}
dis2 = {3:'vaishu' , 4 :'pooja'}

d = dis1.copy()
d.update(dis2)

print(d)
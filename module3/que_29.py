"""
Write a Python program to check multiple keys exists in a dictionary
"""

societymember = {
    'name' : 'priya',
    'flatno' : '240',
    'tower' : 'D',
}
print(societymember.keys() >= {'name','flatno'})
print(societymember.keys() >= {'name','priya'})
print(societymember.keys() >= {'tower','name'})
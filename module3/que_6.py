"""
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.

"""
l1 = [2,4,6,7,2,8]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

#other way to use duplicate element with set

s =set(l1)
print(s)


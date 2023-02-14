"""
Write a Python function that takes two lists and returns true if they have 
at least one common member. 
"""



def list(l1,l2):
    result = False

    for x in l1:
        for y in l2:
            if x == y:
                result= True
                return result

l1 = ['abc','cde','xyz','pqr','rxy']
l2 = ['cab','abc','cde','pqr']
print(list(l1,l2))

l1 = ['abc','cde','xyz','pqr']
l2 = ['cab']
print(list(l1,l2))
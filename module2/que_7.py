"""
Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero
"""
v1 = int(input("Enter value 1 :"))
v2 = int(input("Enter value 2 :"))
v3 = int(input("Enter value 3 : "))

sum = v1+v2+v3

if v1==v2 or v2==v3 or v3==v1:
    print("Zero")

else :
    print(sum)
    

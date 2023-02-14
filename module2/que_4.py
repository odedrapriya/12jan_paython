"""
Write python program that swap two number with temp variable and 
without temp variable.

"""
n1 = int(input("Enter the value of N1 :"))
n2 = int(input("Enter the value of N2 :"))

temp = n1
n1 = n2
n2 = temp

print("swaping value of n1 :",n1)
print("swapping value of n2 :",n2)
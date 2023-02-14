"""
Write a Python script to check if a given key already exists in a 
dictionary. 
"""
d = {1:10, 2:20, 3:30, 4:40, 5:50}
def is_key_present(x):
    if x in d:
        print("Key present in dictionary")
    else:
        print("key is not present in dictionary")

is_key_present(4)
is_key_present(9)


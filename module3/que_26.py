"""
Write a Python script to concatenate following dictionaries to create a 
new one.
"""
dis1 = {1:10 , 2:20}
dis2 = {3:30 , 4:40}
dis3 = {4:40 , 5:50} 
dis4 = {}

for d in (dis1,dis2,dis3):dis4.update(d)
print(dis4)
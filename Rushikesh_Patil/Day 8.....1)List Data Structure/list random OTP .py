
import random 

a=[1,2,3,4,5,6,7,8,9,10]
b=[]
i=0
while i<4:
    num = random.choice(a)
    if num not in b:
        b.append(num)
        i+=1
print(b)







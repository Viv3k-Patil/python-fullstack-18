numbers=[0,1,2,3,4,5,6,7,8,9]
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_char=['@','#','$','!','<',',','&','%']
password=[]
import random
i=0
for num in numbers:
    while i <5:
        b=random.choice(numbers)
        password.append(b)
        i=i+1
j=0
for alpha in alphabet:
    while j<2:
        b=random.choice(alphabet) 
        password.append(b)
        j=j+1
k=0
for alpha in special_char:
    while k<1:
        b=random.choice(special_char) 
        password.append(b)
        k=k+1
password1=''.join(map(str,password))
print("password is ",password1)
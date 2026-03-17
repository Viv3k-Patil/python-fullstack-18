

count=0
for i in range(1,201):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
            count+=1
print("The Total Prime Number Of 1 to 200:",count)
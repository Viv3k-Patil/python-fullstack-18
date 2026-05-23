

count=0
for i  in range(1,501):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
            print(i)
print("The Total prime number of 1 to 500:",count)
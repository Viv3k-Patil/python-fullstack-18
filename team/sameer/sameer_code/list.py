mylist=["apple","banana","apple","cherry","date","apple"]
# a = mylist.remove("apple")
# print(mylist)
# print(a)

a = mylist.pop()
print(mylist)
print(a)


mylist.append("milk")
print(mylist)


mylist.insert(1,"eggs")
print(mylist)

print(len(mylist))



mylist_1=mylist.copy()
print(mylist_1)



mylist_1.sort()
print(mylist_1)

print(mylist_1.count("apple"))

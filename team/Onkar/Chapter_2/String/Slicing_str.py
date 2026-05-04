# Slicing String


string = "ONKAR SAVANJI"
print (string)

print("string[:]", string[:])         #ONKAR SAVANJI
print("string[:3]", string[:3])       #ONK
print("string[6:]", string[6:])       #SAVANJI
print("string[1:5]", string[1:5])     #NKAR
print("string[-4:-1]", string[-4:-1]) #NJI
print("string[-7:]", string[-7:])     #SAVANJI
print("string[:-4]", string[:-4])     #ONKAR SAV
print(string[:8])                     #ONKAR SA
print("string[:8][1:4]",string[:8][1:4])#NKA
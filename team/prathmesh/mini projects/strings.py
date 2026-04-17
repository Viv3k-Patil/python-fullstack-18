my_str=("This Is My First Python Program")

#case conversion
capitalize=my_str.capitalize()
case_fold=my_str.casefold()
lower_str=my_str.lower()
upper_str=my_str.upper()
my_tittle=my_str.title()
swap_case=my_str.swapcase()

#Searching & Finding
find=my_str.find("I")
my_rfind=my_str.rfind("o")
index=my_str.index("M")
r_index=my_str.rindex("M")
count=my_str.count("P") #return count of charecters
starts_with=my_str.startswith("This")#starts with suffix
ends_with=my_str.endswith("pro") #ends with priffix
#print(ends_with)

str=("this is my string")
#Modifying Strings

replace=str.replace("t","T") 
strip=str.strip("*")   #remove extra space in string
lstrip=str.lstrip("*") # Removes only from the left
rstrip=str.rstrip("*") # Removes only from the right
re_priffix=str.removeprefix("th")
re_suffix=str.removesuffix("ing")

#Splitting & Joining
spilit=str.split("-",1) # split from the left, max 1 split
r_spilt=str.rsplit("-",1) # split from the right, max 1 split
spiltness=str.splitlines()
str_join=str.join(["this",])
#print(str_join)

a=("sdk")
#Alignment & Formatting
center=a.center(6,"*")
ljst=a.ljust(5,"-")
rjst=a.rjust(5,"-")
zfill=a.zfill(10)
expand_tabs=a.expandtabs()

#Checking Methods (Boolean)
isalnum=a.isalnum()
isapha=a.isalpha()
print(isapha)
# Dict is mutable, unordered, 
#  key in a dictionary should always be unique!!

# Example 1 :

my_dict = {
    "name" : "Onkar",
    "age" : 11,
    "location" : "Mumbai"

}
print(my_dict)

# Example 2 :

my_batch_details = {
     "batch_number " : 18 , 
     "students": [
         "Onkar",
         "Akshata",
         "Pornima",
         "Sameer",
         "Girish"
     ]
}
print(my_batch_details)

print("Dict_Keys:"  ,my_batch_details.keys())
print("Dict_values :",my_batch_details.values())
print("Dict_items:",my_batch_details.items())

print(type(my_batch_details))

# Example 3 :

sys_env_var = {
    "Git_HOME" : "C:\Program Files\Git\cmd",
    "MAVEN_HOME" : "path"
}
print(sys_env_var)


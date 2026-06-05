
my_dict = {
    "name" : "Akshata",
    "age" : 28,
    "location" : "pune"

}
print(my_dict)

my_batch_details = {
     "batch_number " : 18 , 
     "students": [
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


sys_env_var = {
    "Git_HOME" : "C:\Program Files\Git\cmd",
    "MAVEN_HOME" : "path"
}
print(sys_env_var)
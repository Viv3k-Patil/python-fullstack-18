[1,1,2,3,4,5,6,8]
# ordered, mutable, allowed duplicate

(1,2,3,4,5,6,6)
# ordered, immutable, allowed duplicates

{1,2,3,4,5,6,6}
# unordered, mutable, duplicate allowed

my_dict = {
    "name":"vivek",
    "age": 30,
    "hobbies": {"playing criket", "singing"}
}

my_batch_details_dict = {
    "batch_name": "newgen-python-fullstack",
    "batch_number": 18,
    "students" : [
        "girish",
        "sameer",
        "akshada"
    ]
}

sys_env_var = {
    "JAVA_HOME" : "C:/program files/jdk1.18",
    "MAVEN_HOME" : "path"
}

# print(my_batch_details_dict)
my_dict["name"] = "Vivek Patil"
print(my_dict)

my_batch_details_dict["mode"] = "offline"
print(my_batch_details_dict)



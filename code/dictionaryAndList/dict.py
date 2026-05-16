"""""Create (Adding Items)"""
#Direct Assignment: Add a single item using square brackets
user_data = {
            "Name":"prathmesh",
            "age":"17",
            "lang":"python",
            "surname":"patil"
             
            }
user_data.values()
#user_data["name"] = "Alice"  # Adding a new key-value pair
print(user_data)
#update() Method: Add multiple items at once from another dictionary or iterable
#user_data.update({"age":"17","name":"jay"})

#user (setdefault) value
#user_data.setdefault("age","17")

"""Read (Accessing Items)"""

#Square Brackets: Retrieve a value directly. This raises a KeyError if the key is missing.
#name=user_data["name"]

#get() Method: The dict.get() method is safer because it returns None
# (or a default value) instead of an error if the key is not found.

#age=user_data.get("age")

#Iterating
# for key,val in user_data.items():

#     print(f"{key} {val}")
    
""" Update (Modifying Items)"""    
user_data["age"]=25


"""update() Method: This can also be used to update existing keys with 
values from another dictionary"""

#user_data.update({"Name":"pp"})

#del user_data["age"]

"""POP Method remove last value in list"""
#user_data.pop("surname")

#last_item=user_data.popitem()
#user_data.clear

#print(user_data)


""" Operation      Method /                 SyntaxDescription"""
# Create	  dict[key] = value	      Adds a new key-value pair.
# Read	      dict.get(key)	          Returns the value for a key; safe from errors.
# Update	  dict.update({k: v})	  Modifies existing keys or adds new ones.
# Delete	  dict.pop(key)	          Removes a key and returns its value.



books = {
         "101":
            {
                 "title": "Python 101",
                 "author": "Alice"
            }
        }
# books["101"]={"tittle":"kingsmen",
#               "aothor":"A.J.vines"
#               }
#print(books)
#books.get(101) #Read kartana get method vaprun key ghychi

# for key,val in books.items():
#     print(val,key)

# books.pop()
# del books["101"]



# print(books)

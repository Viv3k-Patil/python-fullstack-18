import logging

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s | %(name)s | [%(levelname)s] | %(message)s",
)


logging.info("hey there")

users=["ram","sham"]

def my_fun(func):
    def wraper(*args):
        if args[0] in users:
            func(*args)
        else:
            print("unorthrised user")
    return wraper        
            
@my_fun            
def accessdata_and_user(name):            
    print("accessing data")
def accessdata_and_user1(name):
    print("accessingg data 1")   
    
accessdata_and_user("sham")    


def my_decoretor(func):
    def my_func(*args):
        print("____________calling the my function {func}")
        func(*args)
        print("_____________ending with my func {func}")
    
    return my_func

@my_decoretor
def grret():    
        return f"this is greet function call"

@my_decoretor 
def greet2(name):
    return f"Hello {name} ,thos is greet2 function  "    

greet2("pp")

user = ["Akshata","Maau","Pratik","Payal"]

def auth_decorator(func):
    def auth_wrapper(*args):
        if args[0] in user:
           func(*args)
        else:
            print("Unautherized access || Login with valid user")
    return auth_wrapper()   
@auth_decorator
def access_private_data(name):
    print("Accessing private data and screate...!")

def access_private_data_2(name):
    print("Accessing private data and screates..!")

access_private_data("Akshata")









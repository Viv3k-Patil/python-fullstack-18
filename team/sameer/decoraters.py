user = ["John", "Alice", "Bob"]

def auth(func):
    def auth_wrapper(*args):
        if args[0] in user:
            func(*args)
        else:
            print("Unauthorized access!! Log in with valid user")
    return auth_wrapper

@auth
def access_private_data(name):
    print("Accessing private data and secrets")

@auth
def access_private_data2(name):
    print("Accessing private data and secrets 2")

access_private_data2("John")
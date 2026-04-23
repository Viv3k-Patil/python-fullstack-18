


# class Instareel():
#     def __init__(self,name,viewcount):
#         self.name=name
#         self.viewcount=viewcount
#         print("running insta reel constructor")

#     def print_username(self):
#         print(self.print_username)
        
#     def view_count(self,):
#         print(self.view_count)  
    
# a=Instareel("vivek",2000)
# b=Instareel("parth",3000)

# print(b.name)
# print(b.viewcount)

class Animal():
    def __init__(self,petname,color,age,brred):
        self.petname=petname
        self.color=color
        self.age=age
        self.brred=brred

    def walking(self):
        print(f"{self.petname} is walking") 

    def speak(self):
        print(f"{self.petname} is speaking")      
         
    def run(self):
        print(f"{self.petname} is running")

    def drink(self):
        print(f"{self.petname} is drinking")       

    def print_basic_info(self):
        print( self.petname)
        print(self.color)
        print(self.age)
        print(self.brred)
        


class dog(Animal):

    def __init__(self, petname, color, age, brred):
        super().__init__(petname, color, age, brred)

    def speak(self):  #method overriding
        print(f"{self.petname} age is {self.age}  ")    

class Cat(Animal):
    def __init__(self, petname, color, age, brred):
        super().__init__(petname, color, age, brred)

    def speak(self):   #method overriding
        print(f"{self.petname} is meowing")    


a=Animal("john","white",5,"Russian")    
b=dog("motu","black",10,"indian-strret")
c=Cat("manimau","milky-white",3,"italian")
# a.speak()
# print(a.brred)
# print(b.brred)
# b.walking()
# print(c.color)
# c.run()
# print("something")
# c.print_basic_info()
a.speak()
c.speak()
b.speak()

             
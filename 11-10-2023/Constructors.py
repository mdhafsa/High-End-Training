#creating a constructer
class cse:
    def __init__(self):
        print("i am default constructer")
    def fun(self):
        print("i am a method in class cse")
obj=cse()  
obj.fun()



#creating a constructer with parameters
class cse:
    def __init__(self,b):
        print("i am default constructer",b)
        print(b)
    def fun(self):
        print("i am a method in class cse")
obj=cse(2)  
obj.fun()
obj.__init__(5)
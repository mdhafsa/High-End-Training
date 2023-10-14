#single inheritence
class parent:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class child(parent):
    def fun3(self):
        print("fun3")
a=parent()
a.fun1()
a.fun2()
b=child()
b.fun3()
b.fun1()  #child class object can access parent methods
b.fun2() 
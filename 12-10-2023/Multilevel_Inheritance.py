#multilevel inheritance
class parent:
    def fun1(self):
        print("parent class ")
        print("fun1")
    def fun2(self):
        print("fun2")
class child(parent):
    def fun3(self):
        print("child class")
        print("fun3")
class gchild(child):
    def fun4(self):
        print("grand child")
        print("fun4")
a=parent()
a.fun1()
a.fun2()
b=child() #b acess parent class methods
b.fun3()
b.fun1()
b.fun2()
c=gchild()
c.fun1()
c.fun2()
c.fun3()
c.fun4()
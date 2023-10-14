'''#single inheritence
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


#multiple inheritance
class father:
    def fun1(self):
        print("father class")
        print("fun1")
class mother:
    def fun2(self):
        print("mother class")
        print("fun2")
class child(father,mother): #takes 1st given class i.e father class
    def fun3(self):
        print("child class")
        print("fun3")
a=father()
a.fun1()
b=mother()
b.fun2()
c=child()
c.fun1()
c.fun2()
c.fun3()


#hierarchical inheritance
class parent:
    def fun1(self):
        print("parent classs")
        print("fun1")
class child1(parent):
    def fun2(self):
        print("child 1 classs")
        print("fun2")
class child2(parent):
    def fun3(self):
        print("child 2 classs")
        print("fun3")
a=parent()
a.fun1()
b=child1()
b.fun2()
b.fun1()
c=child2()
c.fun3()
c.fun1()
#c.fun2()   we cannot access child 1 with child 2 object

'''

#overriding
class parent:
    def fun1(s):
        print("fun1 in parent class")
    def fun2(self):
        print("fun2")
class child(parent):
    def fun1(self):
        print("fun1 in child class")
    def fun2(self):
        print("fun2 in child class")
a=parent()
a.fun1()
a.fun2()
b=child()
b.fun1()
b.fun2()
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
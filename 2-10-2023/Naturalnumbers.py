#print 1 to n values by recursion
def recur(n):
    if(n==0):
        return
    recur(n-1)
    print(n)
n=int(input("enter n value:"))
recur(n)
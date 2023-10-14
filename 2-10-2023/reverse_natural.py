#print n to 1 values using recursion
def recur(n):
    if(n==0):
        return
    print(n)
    recur(n-1)
n=int(input("enter n value:"))
recur(n)
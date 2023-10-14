#sum of array elements using 
'''def fun(l,n):
    s=0
    if n==1:
        return l[0]
    return l[n-1]+fun(l,n-1)
    
n=int(input())
l=list(map(int,input().split()))[:n]
print(fun(l,n))



def fun(l):
    n=len(l)
    if n==1:
        return l[0]
    mid=n//2
    ls=fun(l[:mid])
    rs=fun(l[mid:])
    return ls+rs
n=int(input())
l=list(map(int,input().split()))[:n]
print(fun(l,n))
'''

def fun(l,s,e):
    if s==e:
        return l[s]
    if s>e:
        return -1
    mid=(s+e)//2
    return fun(l,s,mid)+fun(l,mid+1,e)
n=int(input())
l=list(map(int,input().split()))[:n]
print(fun(l,0,n-1))
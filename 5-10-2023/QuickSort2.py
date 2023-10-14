def fun(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]

    left=[i for i in arr if i<pivot]
    right=[i for i in arr if i>pivot]
    return fun(left)+[pivot]+fun(right)
l=list(map(int,input().split(",")))
a=fun(l)
print(*a,sep="->")

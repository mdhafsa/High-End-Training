def quicksort(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def fun(l,start,end):
    if start<end:
        pi=quicksort(l,start,end)
        fun(l,start,pi-1)
        fun(l,pi+1,end)
l=list(map(int,input().split()))
fun(l,0,len(l)-1)
print(l)

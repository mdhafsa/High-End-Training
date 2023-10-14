def bs(l,si,li,se,floor):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==se:
            return l[mid]
        if l[mid]<se:
            floor=l[mid]
            return bs(l,mid+1,li,se,l[mid])
        if l[mid]>se:
            return bs(l,si,mid-1,se,l[mid])
    return floor
l=list(map(int,input().split()))
s=int(input("enter search"))
n=len(l)
ans=bs(l,0,n-1,s,-1)
print(ans)
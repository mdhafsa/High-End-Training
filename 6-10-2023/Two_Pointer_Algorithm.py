#two pointer algo works only on sorted lists
#return the indices of elements which gives target sum
def two_pointer(l,target):
    p1=0
    p2=len(l)-1
    while p1<p2:
        if l[p1]+l[p2]==target:
            return p1,p2
        elif l[p1]+l[p2]>target:
            p2-=1
        elif l[p1]+l[p2]<target:
            p1+=1
        
l=list(map(int,input().split()))
target=int(input())
res=two_pointer(l,target)
print(res)
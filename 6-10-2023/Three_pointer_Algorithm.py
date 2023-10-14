#three pointer algorithm
#return  3 indices of  elements which gives target sum
def three_pointer(l,target):
    p2=len(l)-1
    for p1 in range(len(l)-2):
        p3=p1+1
        if l[p1]+l[p2]+l[p3]==target:
            return (p1,p3,p2)
        elif l[p1]+l[p2]+l[p3]>target:
            p2-=1
        elif l[p1]+l[p2]+l[p3]<target:
            p3+=1
        
l=list(map(int,input().split()))
target=int(input())
res=three_pointer(l,target)
print(res)
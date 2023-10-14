def fun(l,target):
    def bt(start,sum,subset):
           
        if sum==target:
            res.append(subset[:])
            return 
        if sum>target or start==len(l):
            return
        subset.append(l[start])
        bt(start+1,sum+l[start],subset)
        subset.pop()
        bt(start+1,sum,subset)
        
    res=[]
    bt(0,0,[])
    return res
l=list(map(int,input().split()))
n=int(input())
result=fun(l,n)
print(result)
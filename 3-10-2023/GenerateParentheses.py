def generate(n):
    def backtrack(s,left,right):
        if len(s)==n*2:
            result.append(s)
            return #stop that particular call
        if left<n:
            backtrack(s+'(',left+1,right)
        if right<left:
            backtrack(s+')',left,right+1)
    result=[]
    backtrack('',0,0)
    return result
n=int(input())
ans=generate(n)
print(*ans)
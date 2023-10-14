m=int(input("enter knapsack capacity:"))
n=int(input("enter no of weights"))
print("enter weights")
wt=list(map(int,input().split()))[:n]
pr=list(map(int,input().split()))[:n]
perkg=[]
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for weight,profit in l:
    if weight<=m:
        maxpr+=profit
        m-=weight
    else:
        maxpr+=m*(profit/weight)
        break
print(maxpr)
    
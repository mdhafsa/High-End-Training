l=list(map(int,input().split(" ,")))
target=int(input())
le=len(l)-1
for i in range(len(l)-2):
    left=i+1
    right=le
    while(right>left):
        if(l[i]+l[left]+l[right])==target:
            print(l[i],l[left],l[right])
            break
        else:
            right-=1
    
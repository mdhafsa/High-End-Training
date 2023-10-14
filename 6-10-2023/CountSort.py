#count sort
'''l=[2,0,2,1,1,0]
count=[0 for i in range(10)]
for i in range(len(l)):
    count[l[i]]+=1
print(count)
for i in range(1,len(count)):# 1 to 9
    count[i]+=count[i-1]
print(count)
res=[0]*len(l)
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(res)
'''
def count_sort(l):
    length=max(l)+1
    count=[0]*length #create maximum element+1 slots
    for i in l:
        count[i]+=1 #markinfg the frequency of numbers
    print(count)
    for i in range(1,length):
        count[i]=count[i]+count[i-1] #list to access index position in output array
    print(count)
    i=len(l)-1 #start form last element of array
    output=[0]*len(l)
    while i>=0:
        current=l[i]
        count[current]-=1 
        pos=count[current]
        output[pos]=current
        i-=1
    return output
        
l=list(map(int,input().split()))
res=count_sort(l)
print(res)

    
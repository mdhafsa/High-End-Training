#Mergesorting: for the sorted two arrays i.e.,left and right.
'''def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        print(left,right)
        mergel=merge(left,right)
        #print(mergel)
        return mergel
    return l
def merge(left,right):
    res=[]
    i=j=k=0   #left=right=res=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
l=[3,9,3,1,0]
print(mergesort(l))'''


#without the merge function
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0         #left=right=res=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
l=[3,9,3,1,0]
mergesort(l)
print(l)
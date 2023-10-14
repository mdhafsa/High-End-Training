#square root with floor value
n=int(input())
si=0
li=n//2
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)
#exact value of square root
def sqrt_binary_search(number,epsilon=1e-6):
    if number<0:
        raise ValueError("connot  compute the square")
    if number <1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_square=mid*mid
        if mid_square<number:
            left=mid
        else:
            right=mid
    return (left+right)/2
number=17
result=sqrt_binary_search(number)
print(f"the squre root of {number} is approximately",result)
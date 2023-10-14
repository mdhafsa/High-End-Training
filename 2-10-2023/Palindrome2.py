#check whether a string is palindrome or not using n/2 time complexity
s=input()
i=0
j=len(s)-1
while(i<j):
    if(s[i]!=s[j]):
        print("not palindrome")
        break
    i=i+1
    j=j-1
else:
    print("palindrome")
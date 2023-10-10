#find the missing numbers
'''def brute_force(n,arr):
    for i in range(1,n+1):
        if i not in arr:
            return i
n=int(input())
arr=list(map(int,input().split()))
b=brute_force(n,arr)
print(b)'''
#in xor operation oreder doesnot matter
'''def xor_approach(n,arr):
    ans=0
    for i in range(1,n+1):
        ans=ans^i
        if i!=n:
            ans=ans^arr[i-1]
    return ans
n=int(input())
arr=list(map(int,input().split()))
c=xor_approach(n,arr)
print(c)'''
# another approach
   
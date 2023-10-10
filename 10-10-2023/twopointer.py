def two_pointers(arr,target):
    arr.sort()
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return True
        if arr[i]+arr[j]<target:
            i+=1
        if arr[i]+arr[j]<target:
            j-=1
    return False
arr=list(map(int,input().split(",")))
target=int(input())
c=two_pointers(arr,target)
print(c)
#problem you will be given an arry =[3,9,-2,8,7,6,5]
'''def query_subarray_sum(arr,queries):
    n=len(arr)
    ps=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            ps[i]=arr[i]
        else:
            ps[i]=ps[i-1]+arr[i]
            
            
    for query in queries:
        i=query[0]
        j=query[1]
        if i==0:
            print(ps[j],end=" ")
        else:
            print(p[j]-ps[i-1],end=" ")
            
arr=list(map(int,input().split(",")))
queries=input()
a=query_subarray_sum(arr,queries)
print(a)'''
            
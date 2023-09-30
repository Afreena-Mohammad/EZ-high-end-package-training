#1.	After creating an array find out the smallest missing positive integer
#sample input =array=[3,7,-5,-6,0,4]
#output:1
'''l=list(map(int,input().split(" ")))
n=[]
for i in range(max(l)+1):
    if(i>= 0 and i not in l):
        n.append(i)
print(n[0])'''
#printing missing positive numbers without using append
'''l=list(map(int,input().split(" ")))
for i in range(max(l)+1):
    s=False
    for a in l:
        if s==a:
            s=True
            break
    if not s:
        print(i)'''
def findnum(arr,n):
    if(n==0):
        return 1
    i=0
    while i<n:
        if arr[i]>=0 and arr[i]<=n and arr[i]!=arr[arr[i]-1]:
            temp=arr[i]=1
            temp_2=arr[i]
            arr[i]=arr[temp]
            arr[temp]=temp_2
        else:
            i+=1
        for i in range(n):
            if arr[i]!=i+1:
                return i+1
            return n+1
arr=[10,4,-4,1]
n=len(arr)
print(findnum( arr,n))
 


    
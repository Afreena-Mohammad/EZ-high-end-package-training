'''arr=list(map(int,input().split()))
s=int(input())
low=0
high=len(arr)
a=0
for i in range(len(arr)):
    mid=int((low+high)/2)
    if(s==arr[mid]):
        a=1
        break
    elif(s<arr[mid]):
        low=mid+1
if(a==1):
    print("element is found ",mid)
else:
    print("element is not found")'''
    
#binary search
def binary_search(arr):
    low=0
    high=len(arr)
    b=0
    for i in range(len(arr)):
        mid=(low+high)//2
        if s==arr[mid]:
            b=1
            break
        elif(s<arr[mid]):
            low=mid+1
    
arr=list(map(int,input().split()))
s=int(input())
if(b==0):
    print("element not found")
else:
    print("element not found")
    
binary_search(arr)


        
        
def linera_search(arr):
    a=0
    for i in range(len(arr)):
        if(arr[i]==b):
            a=1
            break
    if a==1:
        print("element found ",i)
    else:
        print("not found")
    return a  
arr=list(map(int,input().split()))
b=int(input())
print(linera_search(arr))

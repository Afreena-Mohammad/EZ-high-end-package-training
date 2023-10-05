def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    else:
        p=arr[0]
        left_arr=[i for i in arr if i<p]
        right_arr=[i for i in arr if i>p]
        return quick_sort(left_arr)+[p]+quick_sort(right_arr)
arr=list(map(int,input().split()))
b=quick_sort(arr)
print(b)

    

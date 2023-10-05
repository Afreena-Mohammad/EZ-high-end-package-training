'''def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2    #time complexity O(nlogn)  
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while left[i]<right[j]:
            if left[k]<right[i]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    
arr=list(map(int,input().split(",")))
merge_sort(arr)
print(arr)'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = arr[:middle]
    print(left_half)
    right_half = arr[middle:]
    print(right_half)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    print(left_sorted)
    print(right_sorted)
    return merge(left_sorted, right_sorted)
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

my_list = list(map(int,input().split(",")))
sorted_list = merge_sort(my_list)
print(sorted_list)
            
            
           
    
    
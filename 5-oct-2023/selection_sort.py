def select_sort(a):
    n=len(a)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i] #oreder of time complexity is O(n**2)
a=list(map(int,input().split()))
select_sort(a)
print(a)
        
            
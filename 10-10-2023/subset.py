'''nums =list(map(int,input().split()))
target_sum = int(input())
subsets = []
for i in range(2 ** len(nums)):
    subset = []
    for j in range(len(nums)):
        if (i >> j) & 1:
            subset.append(nums[j])
    if sum(subset) == target_sum:
        subsets.append(subset)
if subsets:
    for subset in subsets:
        print(Subset)
else:
    print(False)'''
def is_pair_exist(arr,target):
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j]==target
               
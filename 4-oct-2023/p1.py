def subset_sum(nums, target):
    def find_subset(current_sum, current_subset, start):
        if current_sum == target:
            subsets.append(current_subset[:])
            return
        if current_sum > target or start == len(nums):
            return

        # Include the current number in the subset
        current_subset.append(nums[start])
        find_subset(current_sum + nums[start], current_subset, start + 1)

        # Exclude the current number from the subset
        current_subset.pop()
        find_subset(current_sum, current_subset, start + 1)

    subsets = []
    find_subset(0, [], 0)
    return subsets

# Test the function with your numbers and target sum
nums = [6, 8, 9, 5, 4, 3, 26, 2]
target_sum = 28
result = subset_sum(nums, target_sum)

if result:
    for subset in result:
        print(subset)
else:
    print("No subsets found that sum up to the target.")
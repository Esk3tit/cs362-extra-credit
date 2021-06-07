# We only need to consider TWO numbers for a sum (not quite subset sum level yet)
def two_sum(nums, target):
    # Use double for loop
    # Offset inner loop by 1 so that the same element/num is not being used twice
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            # If sum of the two numbers is target then return array with those two numbers
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]


# print(two_sum([3, 2, 4], 6))

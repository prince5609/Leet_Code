def searchInsert(nums, target):
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return print(i)
    else:
        if nums[-1] > target:
            for i in range(len(nums)):
                if nums[i] > target:
                    return print(i)
        else:
            return print(len(nums))


searchInsert([1], 1)

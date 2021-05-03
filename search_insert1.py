def searchInsert(nums,target):
    if target in nums:
        if len(nums)>=2:
            s = 0
            l = len(nums) - 1
            m = int((l - s) / 2)
            while s < l:
                if nums[s] == target:
                    return s
                elif nums[l] == target:
                    return l
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    s = m + 1
                    m = int(((l - s) / 2) + s)
                elif target < nums[m]:
                    l = m - 1
                    m = int(((l - s) / 2) + s)
        else:
            return 0

    else:
        if nums[-1]<target:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
print(searchInsert([1],1))
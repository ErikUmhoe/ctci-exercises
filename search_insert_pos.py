def searchInsert(nums, target):
    numLen = len(nums)
    mid = numLen // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        if mid == 0 or nums[mid-1] < target:
            return mid
        return searchInsert(nums[:mid], target)
    elif nums[mid] < target:
        if mid+1 >= numLen or nums[mid+1] > target:
            return mid + 1
        return searchInsert(nums[mid+1:], target)  + mid + 1
    
    
    
arr = [1,3,5,6]
print(searchInsert(arr, 5)) # return 1
print(searchInsert(arr, 2))
print(searchInsert(arr,7))
    
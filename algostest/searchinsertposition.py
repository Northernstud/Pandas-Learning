def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high: 
        mid = low + (high - low) // 2
        print(low, mid, high)

        if target > nums[mid]: 
            low = mid + 1

        elif target < nums[mid]:
            high = mid -1
        
        else:
            return mid

    return low

a = int(input("number in the array:"))
print(searchInsert([1, 3, 5, 6], a))
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    n = 0

    for i in nums:
        if i != val:
            nums[n] = i
            n += 1
    
    return n
        

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))
# print(nums)
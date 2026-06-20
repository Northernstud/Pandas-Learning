from typing import List
from timeit import timeit




# most generic obv solution
def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                result.append(i)
                result.append(j)
                return result
            
# cool solution by me
def twoSumtwo(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] + nums[j+1] == target:
                result.append(i)
                result.append(j+1)
                return result

def twoSumthree(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

result = timeit(
    lambda: twoSumthree([2, 7, 11, 15], 9),
    number=10000
)


print(result)  # total seconds for 10,000 runs
print(result / 10000)  # average seconds per run   
print(twoSumthree([2,7,11,15], 9))
#bad solution
def removedup(nums: list) -> int:
    r = []
    i = 0
    for n in nums:
        if n not in r:
            r.append(n)
            nums[i] = n
            i += 1
    return len(r)

#ez less time and less memory
def removedup2(nums: list) -> int:
    r = 0
    for i in range(len(nums)):
        if nums[i] != nums[r] and i != r:
            nums[r+1] = nums[i]
            r += 1

    return r+1


print(removedup2([1,2,3,4]),)



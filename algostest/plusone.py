def plusOne(digits: List[int]) -> int: 
    index = len(digits) - 1
    a = 0
    while index >= 0:
        print((digits[index] + 1 )// 10)
        if (digits[index] + 1 )// 10 == 0: 
            digits[index] = digits[index] + 1
            break
        else: 
            print("hi", index, digits[index])
            digits[index] = 0
            print(digits[index])
            if index == 0:
                print("works")
                digits.insert(0, 1)
            
            index -= 1
    return digits

print(plusOne([1, 2, 3]))
        
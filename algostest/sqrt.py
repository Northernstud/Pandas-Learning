# my first solution O(sqrt(x))
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x < 3: 
        return 1
    for i in range(x):
        print(i)
        if i * i > x:
            print("if")
            return i-1
        elif i * i == x:
            print("elif")
            return i
        
# my better solution: 
def mySqrt2( x: int) -> int: 
    low = 0
    high = x
    while low <= high:
        
        
        mid = low + (high - low) // 2

        if mid * mid == x:
            return mid
        
        if mid * mid < x:
            low = mid + 1
        if mid * mid > x:
            high = mid - 1

    if mid * mid > x: 
        return mid - 1
    else: 
        return mid
        return mid

print(mySqrt2(8))
print(2**31 - 46340**2)

test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (15, 3),
    (16, 4),
    (17, 4),
    (24, 4),
    (25, 5),
    (26, 5),
    (35, 5),
    (36, 6),
    (37, 6),
    (49, 7),
    (50, 7),
    (63, 7),
    (64, 8),
    (65, 8),
    (99, 9),
    (100, 10),
    (101, 10),
    (1000, 31),
    (1024, 32),
    (1025, 32),
    (9999, 99),
    (10000, 100),
    (10001, 100),
    (1000000, 1000),
    (2147395599, 46339),
    (2147395600, 46340),
    (2147395601, 46340),
    (2147483646, 46340),
    (2147483647, 46340),
]

# Example usage:
for x, expected in test_cases:
    result = mySqrt2(x)  # replace with your function
    status = "PASS" if result == expected else "FAIL"
    print(status)
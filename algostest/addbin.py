# Given two binary strings a and b, return their sum as a binary string.

# Input: a = "11", b = "1"
# Output: "100"

# streak post 

def addTwoBin(a: str, b: str) -> str:
    ia = len(a) - 1
    ib = len(b) - 1
    z = 0 
    r = []

    while ia >= 0 or ib >= 0 or z == 1:
        x = (int(a[ia]) if ia >= 0 else 0 )+ (int(b[ib]) if ib >= 0 else 0 )+ z

        if x == 3: 
            r.append("1")
            z = 1
        elif x == 2: 
            r.append("0")
            z = 1
        else: 
            r.append(str(x))
            z = 0

        ia -= 1 
        ib -= 1

    return "".join(reversed(r))

# better solition



print(addTwoBin("1011", "1010"))

tests = [
    ("0", "0", "0"),
    ("1", "0", "1"),
    ("0", "1", "1"),
    ("1", "1", "10"),
    ("10", "1", "11"),
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
    ("100", "100", "1000"),
    ("111", "1", "1000"),
    ("1111", "1111", "11110"),
    ("10101", "0", "10101"),
    ("0", "10101", "10101"),
    ("100000", "1", "100001"),
    ("111111", "1", "1000000"),
    ("1001", "110", "1111"),
    ("101", "11", "1000"),
    ("110010", "101101", "1011111"),
    ("1000001", "111111", "10000000"),
    ("111000", "111", "111111"),
    ("101010101", "101010101", "1010101010"),
]

# Assuming your solution is:
# def addBinary(a: str, b: str) -> str:
#     ...

for i, (a, b, expected) in enumerate(tests, start=1):
    result = addTwoBin(a, b)  # Replace with your function call
    if result == expected:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL")
        print(f"  a        = {a}")
        print(f"  b        = {b}")
        print(f"  expected = {expected}")
        print(f"  got      = {result}")
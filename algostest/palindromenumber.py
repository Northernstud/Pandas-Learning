def isPalindrome(x: int) -> bool:
    if x < 0: 
        return False

    b = 0
    a = x

    while x != 0:
        b = b * 10 + x % 10
        x = x // 10

    return a == b

#better solution for this is just reverse one half of the x
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10

    return x == reversed_half or x // 10 == reversed_half

print(isPalindrome(0))
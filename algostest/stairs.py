# too slow
def inorderTraversal(n: int) -> int:
    
    a = [1, 2]
    t = True

    if n == 2 or n == 1:
        return n

    while t: 
        b = len(a)
        for i in range(len(a)):
            if a[i] + 2 <= n:
                a[i] += 1
                a.append(a[i]+2)

            if b == len(a):
                return b
        

    return len(a)

import math

#try cool method
def climb(n: int) -> int:
    r = 1
    b = 2

    while n - b >= 0: 
        r += math.factorial(n - (b // 2)) // (math.factorial(n - b) * math.factorial(b//2))
        b += 2

    return r



for i in range(1, 46):
    print(i, climb(i))

# print(inorderTraversal(30))

#fib
def climb2(n: int) -> int:
    a, b = 1, 2      # a = f(1), b = f(2)
    for _ in range(n - 2):
        a, b = b, a + b
    return b if n >= 2 else 1
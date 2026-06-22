def maxNumberOfBalloons(text: str) -> int:
    w = "balloon"
    s = ""
    p = {
        "b": 1,
        "a": 1,
        "l": 2,
        "o": 2,
    }

    for l in text:
        if l in w: 
            s += l

    result = s.count("b")
    
    for i in s:
        if i == "o" or i == "l":
            print(0)

# not optimal because uses count           
def maxNumberOfBalloons2(text: str) -> int:
    l = "balon"
    r = []

    for i in l:
        if i == "o" or i == "l":
            r.append(text.count(i)//2)
        else:
            r.append(text.count(i))
    
    return min(r)

def max(text: str) -> int:
    b = a = l = o = n = 0

    for e in text:
        match e:
            case "b":
                b += 1
            case "a":
                a += 1
            case "l":
                l += 1
            case "o":
                o += 1
            case "n":
                n += 1
    
    return min(b, a, l // 2, o // 2, n)


print(maxNumberOfBalloons2("leetcode"))
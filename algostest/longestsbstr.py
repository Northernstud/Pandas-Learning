

def length_of_sub_str(s: str):
    if (s == ""):
        return 0
    used = ""
    answers = [1]
    for i, el1 in enumerate(s): 
        used = el1
        for j, el2 in enumerate(s):
            if j > i: 
                if el2 not in used:
                    used = used + el2
                    if j == len(s)-1:
                        answers.append(len(used))
                elif el2 in used: 
                    answers.append(len(used))
                    break
    return(max(answers))

# print(length_of_sub_str("ab"))



# Solution hehe
def lengthOfSubStr(s: str):
    if (s == ""):
        return 0
    r = [1]
    used = ""
    x = [1]
    for i, el in enumerate(s):
        # print(s[i+1:], s[i+1:].find(el), s[i : i + s[i+1:].find(el)+1])
        a = s[i + 1:]
        if a.find(el) == -1:
            #print(-1)
            used = s[i]
            for j, el2 in enumerate(a):
                if el2 not in used:
                    used = used + el2
                    if j == len(a)-1:
                        x.append(len(used))
                elif el2 in used: 
                    x.append(len(used))
                    break
        else:
            #print("else")
            l = s[i + 1 : i + s[i+1:].find(el)+1]
            used = s[i]
            for j, el2 in enumerate(l):
                if el2 not in used:
                    used = used + el2
                    if j == len(l)-1:
                        x.append(len(used))
                elif el2 in used: 
                    r.append(len(used))
                    break
    
    else:
        return max(max(x), max(r))

print(lengthOfSubStr("abba"))








tests = {
    "abcabcbb": 3,
    "bbbbb": 1,
    "pwwkew": 3,
    "": 0,
    "a": 1,
    "aa": 1,
    "ab": 2,
    "abcdef": 6,
    "abcdefghijklmnopqrstuvwxyz": 26,
    "a b c": 3,
    "dvdf": 3,
    "tmmzuxt": 5,
    "abba": 2,
    "abcabcabc": 3,
    "aab": 2,
    "1234567890": 10,
    "112233": 2,
    "a1b2c3a1": 6,
    "aA": 2,
    "AaAa": 2,
    "abcbb": 3,
    "bbabc": 3,
    "abcba": 3,
    "aaaaabcdef": 6,
    "abcdefaaaaa": 6,
    "ababababab": 2,
    "abcabcbbcc": 3,
    "abcdeafghij": 10,
    "abcdcba": 4,
    "abcxabc": 4,
    "aababcabcd": 4,
    "abcdea": 5,
    "abcdda": 4,
    "aabaab": 2,
    "wobgrovw": 6,
    "anviaj": 5,
    "ohvhjdml": 6,
    "a!a!b@b@c": 3,
    "abcdefaghij": 7,
    "xyzxyzxy": 3,
    "mississippi": 2,
}

passed = 0
failed = 0
for s, expected in tests.items():
    result = lengthOfSubStr(s)
    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAIL: {s!r} -> got {result}, expected {expected}")

print(f"\n{passed} passed, {failed} failed out of {len(tests)}")

print(lengthOfSubStr("pwwkew"))







# print(lengthOfSubStr("ab"))
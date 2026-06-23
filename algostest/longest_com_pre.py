from typing import List

# my 1st solution 
def longestCommonPrefix2(strs: List[str]) -> str:
    result = ""
    l = 0
    if "" in strs:
        return ""

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i < len(strs[j]):
                if strs[0][i] == strs[j][i]:
                    l = 0
                else: 
                    l += 1
                    break
            else:
                l +=1
                break
        if l == 0:
            result += strs[0][i]
        else: 
            break

    return result

# better solution return everything from 0 if we foind the different one 
def longestCommonPrefix3(strs: List[str]) -> str:
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return strs[0][:i]
    
    return strs[0]
    



tests = [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    (["interspecies","interstellar","interstate"], "inters"),
    (["hello"], "hello"),
    (["a"], "a"),
    (["abc","def","ghi"], ""),
    (["flower","flow","flop"], "flo"),
    (["prefix","preach","prevent"], "pre"),
    (["","abc","abcd"], ""),
    (["","",""], ""),
    (["abc","",""], ""),
    (["test","test","test"], "test"),
    (["a","ab","abc"], "a"),
    (["car","cat","can"], "ca"),
    (["zebra","apple","apricot"], ""),
    (["flower", "flo", "flow"], "flo")
]

for value, expected in tests:
    result = longestCommonPrefix3(value)
    print(value, result, "✓" if result == expected else "✗")


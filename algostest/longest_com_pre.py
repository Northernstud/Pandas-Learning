from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    for i in range(len(strs[0])):
        if i < len(strs[1]) and i < len(strs[2]) and strs[0][i] == strs[1][i] and strs[2][i] == strs[1][i]:
            result += strs[0][i]
    return result

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
    (["zebra","apple","apricot"], "")
]

for value, expected in tests:
    result = longestCommonPrefix(value)
    print(value, result, "✓" if result == expected else "✗")
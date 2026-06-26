def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        for j in range(len(needle)):
            if i + j < len(haystack) and haystack[i+j] == needle[j]:
                if j == len(needle) - 1:
                    return i
            else: 
                break

    return -1

#need to learn KMP

print(strStr("mississippi", "issip"))

tests = [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("mississippi", "issip", 4),
    ("abcde", "e", 4),
    ("abcde", "a", 0),
    ("abcde", "abcde", 0),
    ("abcde", "abcdex", -1),
    ("banana", "ana", 1),
    ("banana", "nana", 2),
    ("abababab", "abab", 0),
    ("abababab", "baba", 1),
    ("abababab", "abac", -1),
    ("aaaaaa", "aaa", 0),
    ("aaaaab", "aaab", 2),
    ("aaaabaaaab", "aaab", 1),
    ("xyzxyzxyz", "xyzx", 0),
    ("xyzxyzxyz", "yzxy", 1),
    ("thequickbrownfox", "brown", 8),
    ("thequickbrownfox", "fox", 13),
    ("thequickbrownfox", "dog", -1),
    ("abcabcabcd", "abcabcd", 3),
    ("aabaaabaaac", "aabaaac", 4),
    ("aaaaaaaaab", "aaab", 6),
    ("abcdabcabcd", "abcabcd", 4),
    ("zzzzzzzz", "zzz", 0),
    ("zzzzzzzz", "zzzzz", 0),
    ("abababca", "abca", 4),
    ("abcabcabcabc", "cabca", 2),
]


for value, needle, expected in tests:
    result = strStr(value, needle)
    print(value, needle, result, "✓" if result == expected else "✗")
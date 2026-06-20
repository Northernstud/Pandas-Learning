# first solution that cam to mind
def romanToInt(s: str) -> int:
    result = 0
    skip = False
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(s)): 
        if skip:
            skip = False
            continue
        if i + 1 < len(s):
            if roman[s[i]] < roman[s[1+i]]:
                result += roman[s[1+i]] - roman[s[i]]
                skip = True
            else: 
                result += roman[s[i]]
        else: 
            result += roman[s[i]]

    return result

def romanToInt2(s: str) -> int:
    result = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(s)): 
        if i + 1 < len(s) and roman[s[i]] < roman[s[1+i]]:
            result -=roman[s[i]]
        else: 
            result += roman[s[i]]

    return result

tests = [
    ("I", 1),
    ("III", 3),
    ("V", 5),
    ("VIII", 8),
    ("X", 10),
    ("XX", 20),

    ("IV", 4),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),

    ("LVIII", 58),      # 50 + 5 + 3
    ("MCMXCIV", 1994),  # 1000 + 900 + 90 + 4
    ("MMXXVI", 2026),
    ("MMMCMXCIX", 3999), # largest standard Roman numeral

    ("XIV", 14),
    ("XIX", 19),
    ("XLIV", 44),
    ("XCIX", 99),
    ("CDXLIV", 444),
    ("CMXCIX", 999),
]

for roman, expected in tests:
    result = romanToInt2(roman)
    print(roman, result, "✓" if result == expected else "✗")
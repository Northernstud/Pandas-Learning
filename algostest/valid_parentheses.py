# My solution i used hint tho 
def isValid(s: str) -> bool:
    stack = []

    for el in s:
        if el == "[" or el == "(" or el == "{":
            stack.append(el)
        if len(stack) == 0:
            return False
        else:
            match el:
                case "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else: 
                        return False
                case ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else: 
                        return False
                case "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else: 
                        return False
    return len(stack) == 0

#better solution?
def isValid2(s: str) -> bool:
    p = {
        "}": "{",
        "]": "[", 
        ")": "("
    }
    
    stack = []

    for el in s:
        if el not in p:
            stack.append(el)
        elif len(stack) == 0 or stack[-1] != p[el]:
            return False
        else:
            stack.pop()

    return len(stack) == 0



test_cases = [
    # ===== Basic valid =====
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("()[]{}", True),
    ("([])", True),
    ("{[]}", True),
    ("([{}])", True),
    ("((()))", True),
    ("[[[]]]", True),
    ("{{{}}}", True),

    # ===== Sequential valid =====
    ("()()()", True),
    ("[][][]", True),
    ("{}{}{}", True),
    ("()[]{}()[]{}", True),
    ("[]{}()[]{}()", True),

    # ===== Nested valid =====
    ("({[]})", True),
    ("{[()()]}", True),
    ("[{()}([])]", True),
    ("(()[]{}())", True),
    ("{({[[]]})}", True),

    # ===== Deep nesting =====
    ("((((((((()))))))))", True),
    ("[[[[[[[[]]]]]]]]", True),
    ("{{{{{{{{}}}}}}}}", True),
    ("({{{[[[]]]}}})", True),
    ("[({({[]})})]", True),

    # ===== Single character invalid =====
    ("(", False),
    ("[", False),
    ("{", False),
    (")", False),
    ("]", False),
    ("}", False),

    # ===== Wrong matching =====
    ("(]", False),
    ("[)", False),
    ("{)", False),
    ("{]", False),
    ("[}", False),
    ("(}", False),

    # ===== Wrong nesting order =====
    ("([)]", False),
    ("[(])", False),
    ("{[(])}", False),
    ("([{})]", False),
    ("{[()]}]", False),

    # ===== Missing closing brackets =====
    ("(()", False),
    ("((())", False),
    ("[[[]]", False),
    ("{{{}", False),
    ("({[]}", False),

    # ===== Extra closing brackets =====
    ("())", False),
    ("()))", False),
    ("[]]", False),
    ("{}}", False),
    ("({[]})]", False),

    # ===== Starts correctly, fails later =====
    ("([][]{}{})]", False),
    ("{[()()]}}", False),
    ("(((())))(", False),
    ("{[({})]}(", False),
    ("[({})](]", False),
]

for s, expected in test_cases:
    result = isValid2(s)
    print(s, result, "✓" if result == expected else "✗")
    
print(isValid2("()"))
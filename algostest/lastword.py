def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[len(s.strip().split(" ")) - 1].strip())

print(lengthOfLastWord("helo     dsfs    world     sdfsfs    "))
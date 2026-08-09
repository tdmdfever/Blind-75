def is_valid(self, s: str) -> bool:
    record = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            recent = record.pop() if record else ' '
            if pairs[char] != recent:
                return False
        else:
            record.append(char)

    return not record

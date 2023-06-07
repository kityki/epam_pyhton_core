def get_longest_word(s: str) -> str:

    s = s.strip().split()
    longest_word = max(s, key=len)
    return longest_word


print(get_longest_word("Python is simple and effective!"))

def replacer(s: str) -> str:

    reversed_table = str.maketrans({'"': "'", "'": '"'})
    s = s.translate(reversed_table)
    return s

def check_str(s: str):
    new_str = ""
    s = s.lower().replace(" ", "")
    for char in s:
        if char.isalpha() or char.isdigit():
            new_str += char
    if new_str == new_str[::-1]:
        return True
    else:
        return False


print(check_str("Live on time, emit no evil"))

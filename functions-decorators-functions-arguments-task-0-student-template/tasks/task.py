from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    lst = [k for k in range(1, num + 1)]
    lst2 = [i ** 2 for i in lst]
    my_dict = dict(zip(lst, lst2))
    return my_dict

print(generate_squares(6))

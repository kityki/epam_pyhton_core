from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s = sorted(s.lower())
    j = 0
    my_dict = {i: s.count(i) for i in set(s)}
    return my_dict




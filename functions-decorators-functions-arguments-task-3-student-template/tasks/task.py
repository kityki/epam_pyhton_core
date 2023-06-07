from typing import List, Dict

from collections import Counter

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    res = {k for d in args for k in d.keys()}
    another_dict = dict.fromkeys(res, 0)
    for d in args:
        another_dict = dict(Counter(another_dict) + Counter(d))
    return another_dict

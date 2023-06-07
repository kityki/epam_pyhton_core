from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    b = []
    for i in lst:
        b.extend([i, i])
    b = b[1:-1]
    new_lst = []
    for i in range(0, len(b)):
        new_lst.append(lst[i:i + 2])
    new_lst = [tuple(i) for i in new_lst]
    super_lst = []
    for t in new_lst:
        if len(t) == 2:
            super_lst.append(t)
    return super_lst



from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    new_lst = []
    for t in lst:
        for el in t.values():
            new_lst.append(el)
    return set(new_lst)


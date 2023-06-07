from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:

    str_list = set(str_list)
    str_list = list(str_list)
    str_list = sorted(str_list)

    return str_list


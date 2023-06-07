from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    try:
        lst = []
        for i in sequence:
            lst += linear_seq(i)
        return lst
    except:
        return [sequence]



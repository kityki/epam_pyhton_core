from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    num = str(num)
    int_tuple = tuple([int(i) for i in num])
    return int_tuple

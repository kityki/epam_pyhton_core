from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total_sum = 0
    for el in sequence:
        if isinstance(el, list) or isinstance(el, tuple):
            total_sum += seq_sum(el)
        else:
            total_sum += el
    return total_sum


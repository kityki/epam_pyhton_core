from typing import List


def foo(nums: List[int]) -> List[int]:
    num_lst = []
    for i in nums:
        nums_product = 1
        for j in nums:
            if j != i:
                nums_product = nums_product * j
        num_lst.append(nums_product)
    return num_lst


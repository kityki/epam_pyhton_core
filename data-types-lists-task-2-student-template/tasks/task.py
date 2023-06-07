from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    my_lst = [i for i in range(1, n + 1)]

    for i in range(len(my_lst)):
        if my_lst[i] % 3 == 0 and my_lst[i] % 5 == 0:
            my_lst[i] = "FizzBuzz"
        elif my_lst[i] % 3 == 0:
            my_lst[i] = "Fizz"
        elif my_lst[i] % 5 == 0:
            my_lst[i] = "Buzz"

    return my_lst


print(get_fizzbuzz_list(17))

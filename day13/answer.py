import json
import math
from itertools import zip_longest
from typing import List, Union
from functools import cmp_to_key


def isRightOrder(
    data1: Union[int, List[int], None], data2: Union[int, List[int], None]
):

    if data1 is None:
        return -1
    if data2 is None:
        return 1
    if isinstance(data1, int) and isinstance(data2, int):
        return data1 - data2

    data1 = data1 if isinstance(data1, list) else [data1]
    data2 = data2 if isinstance(data2, list) else [data2]

    return next(
        filter(
            lambda x: x != 0,
            (isRightOrder(ele1, ele2) for ele1, ele2 in zip_longest(data1, data2)),
        ),
        0,
    )


def main():
    with open("input.txt", "r") as f:
        packets = [
            tuple(map(json.loads, datas.splitlines()))
            for datas in f.read().strip().split("\n\n")
        ]

    answer_1 = sum(
        i
        for i, (data1, data2) in enumerate(packets, 1)
        if isRightOrder(data1, data2) < 0
    )
    print(f"answer part 1 is: {answer_1}")

    packets = list(sum(packets, ()))
    packets_ordered = sorted(packets + [[[2]], [[6]]], key=cmp_to_key(isRightOrder))

    gen_find_delimiter = (
        i
        for i, packet in enumerate(packets_ordered, 1)
        if packet == [[2]] or packet == [[6]]
    )

    answer_2 = next(gen_find_delimiter) * next(gen_find_delimiter)

    print(f"answered part 2 is: {answer_2}")


if __name__ == "__main__":
    main()

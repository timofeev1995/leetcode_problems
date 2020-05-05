from typing import List


def find_complement(num: int) -> int:
    """

    :param num: `int` to found complement for
    :return: `int` binary complement.
    """
    # Idea is simple: lets make 2-base integer as usual, but
    # instead of appending `1` in case of remainder == 1 we will append 0.
    # It is our 2-base complement.
    if num == 0:
        return 1

    complement_bits = []
    while num != 0:
        remainder = num % 2
        num = num // 2
        complement_bits.append(int(remainder != 1))
    return sum([(2 ** i) * x for i, x in enumerate(complement_bits)])


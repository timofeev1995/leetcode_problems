def add_binary(a: str, b: str) -> str:
    """

    :param a: `str` with base-2 number
    :param b: `str` with base-2 number
    :return: `str` with base-2 number which is sum of a and b
    """
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    if a[-1] == '1' and b[-1] == '1':
        return add_binary(add_binary(a[0:-1], b[0:-1]), '1') + '0'
    elif a[-1] == '0' and b[-1] == '0':
        return add_binary(a[0:-1], b[0:-1]) + '0'
    else:
        return add_binary(a[0:-1], b[0:-1]) + '1'

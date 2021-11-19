def count_days(weights, capacity):
    current = 0
    days = 1
    for w in weights:
        if current + w > capacity:
            days += 1
            current = 0
        current += w
    return days


def ship_within_days(weights, days):
    lower_bound = max(weights)
    higher_bound = sum(weights)

    while lower_bound < higher_bound:
        mid = lower_bound + (higher_bound - lower_bound) // 2
        days_to_ship = count_days(weights, mid)

        if days_to_ship > days:
            lower_bound = mid + 1
        else:
            higher_bound = mid

    return lower_bound


if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    assert ship_within_days(weights, days) == 15

    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    assert ship_within_days(weights, days) == 6

    weights = [1, 2, 3, 1, 1]
    days = 4
    assert ship_within_days(weights, days) == 3

    weights = [
        361, 321, 186, 186, 67, 283, 36, 471, 304, 218, 60, 78, 149, 166, 282, 384,
        61, 242, 426, 275, 236, 221, 27, 261, 487, 90, 468, 19, 453, 241
    ]
    days = 15
    print(ship_within_days(weights, days))
    assert ship_within_days(weights, days) == 660


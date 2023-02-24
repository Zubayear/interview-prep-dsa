def number_of_ways_to_make_change(total, denominator_arr):
    """
    Space = O(N) -> N is total
    Time = O(Nd) -> N is total, d is denominator_arr
    @param total: 10
    @param denominator_arr: [1, 5, 10, 25]
    @return:
    """
    # ways = [1, 0, 0, ...
    ways = [0 for _ in range(total + 1)]
    ways[0] = 1
    for denominator in denominator_arr:
        for amount in range(1, total + 1):
            if denominator <= amount:
                ways[amount] += ways[amount - denominator]
    return ways[total]


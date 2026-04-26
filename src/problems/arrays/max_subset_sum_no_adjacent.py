def max_subset_sum_no_adjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    first, second = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        value = max(second, first + array[i])
        first = second
        second = value
    return second

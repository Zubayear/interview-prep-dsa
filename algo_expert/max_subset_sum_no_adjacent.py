def max_subset_sum_no_adjacent(array):
    # [7,10,12,7,9,14]
    # if len(array) < 3:
    #     return max(array[0], array[1])
    # aux_array = []
    # aux_array.insert(0, array[0])
    # aux_array.insert(1, max(array[0], array[1]))
    # for i in range(2, len(array)):
    #     value = max(aux_array[i-1], aux_array[i-2] + array[i]) # at 2nd index max(10, 7+12)
    #     aux_array.insert(i, value)
    # return aux_array[-1]
    first, second = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        # [7,10,12,7,9,14]
        #  f s
        #    f s=19
        # for index 3 i.e. 7 we have 10, 19, 7
        # f=19 s=19
        # 19 19 9 => max(19, 19+9) => 28
        # 19 28 14 => max(28, 19+14) => 33
        value = max(second, first + array[i]) # 19
        first = second
        second = value
    return second
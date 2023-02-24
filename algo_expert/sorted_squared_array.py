def squared_array(array):
    # [-1,-6,-1,2,3]
    #  p1         p2
    p1, p2 = 0, len(array) - 1
    output_array = []
    insert_pos = len(output_array) - 1
    while p1 <= p2:
        if abs(array[p1]) >= abs(array[p2]):
            output_array.insert(insert_pos, abs(array[p1]) * abs(array[p1]))
            p1 += 1
        else:
            output_array.insert(insert_pos, abs(array[p2]) * abs(array[p2]))
            p2 -= 1
        insert_pos -= 1
    return output_array
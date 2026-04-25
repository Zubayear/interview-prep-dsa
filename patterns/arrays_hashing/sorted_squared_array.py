def squared_array(array):
    left, right = 0, len(array) - 1
    output = [0] * len(array)
    pos = len(array) - 1
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            output[pos] = array[left] * array[left]
            left += 1
        else:
            output[pos] = array[right] * array[right]
            right -= 1
        pos -= 1
    return output

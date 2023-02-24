def max_sum_increasing_subsequence(arr):
    # [8,12,2,3,15,5,7]
    sums = arr[:]
    sequence_res = [-1 for _ in range(len(arr))]
    max_res = -1
    max_idx = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and arr[i] + sums[j] > sums[i]:
                sums[i] = arr[i] + sums[j]
                sequence_res[i] = j
        if max_res < sums[i]:
            max_res = sums[i]
            max_idx = i
    res = []
    while max_idx != -1:
        res.append(arr[max_idx])
        max_idx = sequence_res[max_idx]

    return max_res, list(reversed(res))
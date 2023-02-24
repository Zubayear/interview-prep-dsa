

import collections
from typing import List


def find_max_sliding_window(nums: List[int], k: int) -> List[int]:
    queue = collections.deque()
    res = [0] * (len(nums) - k + 1)
    for i in range(k):
        if len(queue) == 0:
            queue.append(nums[i])
        elif queue[0] > nums[i]:
            queue.append(nums[i])
    res[-1] = queue.popleft()

    # print(queue)

    idx = 1
    for i, window_end in enumerate(nums):
        if i == 0:
            continue
        if queue[-1] > window_end:
            queue.append(window_end)
        if i >= k - 1 or queue[-1] < window_end:
            res[idx] = queue.popleft()
            idx += 1
    return res
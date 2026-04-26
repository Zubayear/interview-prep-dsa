import collections
from typing import List


def find_max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums or k > len(nums):
        return []

    queue = collections.deque()
    res = []

    for i, num in enumerate(nums):
        while queue and queue[0] <= i - k:
            queue.popleft()

        while queue and nums[queue[-1]] <= num:
            queue.pop()

        queue.append(i)

        if i >= k - 1:
            res.append(nums[queue[0]])

    return res

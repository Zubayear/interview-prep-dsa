import collections


def first_neg_number(nums, k):
    res = []
    q = collections.deque()
    l, r = 0, 0

    while r < len(nums):
        val = nums[r]
        if val < 0:
            q.append(val)
        if r - l + 1 < k:
            r += 1
        elif r - l + 1 == k:
            if q:
                cur = q[0]
                res.append(cur)
                if cur == nums[l]:
                    q.popleft()
            else:
                res.append(0)
            r += 1
            l += 1
    return res
from typing import List


class Solution:

  @staticmethod
  def climb_stairs(n: int) -> int:
    if n == 0 or n == 1: return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

  @staticmethod
  def tribonacci(n: int) -> int:
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(3, n+1):
      curr = t0 + t1 + t2
      t0 = t1
      t1 = t2
      t2 = curr
    return t2

  @staticmethod
  def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 2: return max(nums[0], nums[1])
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = nums[1]

    for i in range(2, n):
      dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[n-1]

  @staticmethod
  # o(2^(m+n)) | o(m+n)
  # memoize = o(m*n) | o(m*n) + o(m+n)
  def unique_paths(m: int, n: int) -> int:
    if m == 0 and n == 0: return 1
    if m < 0 or n < 0: return 0
    # Count all paths coming from up
    up = Solution.unique_paths(m-1, n)
    left = Solution.unique_paths(m, n-1)
    return up + left

  
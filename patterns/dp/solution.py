from typing import List


class Solution:

  @staticmethod
  def climb_stairs(n: int) -> int:
    if n <= 1:
      return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
      prev2, prev1 = prev1, prev1 + prev2
    return prev1

  @staticmethod
  def tribonacci(n: int) -> int:
    if n == 0:
      return 0
    if n in (1, 2):
      return 1
    t0, t1, t2 = 0, 1, 1
    for _ in range(3, n + 1):
      t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2

  @staticmethod
  def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0
    for num in nums:
      prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1

  @staticmethod
  def unique_paths(m: int, n: int) -> int:
    if m <= 0 or n <= 0:
      return 0
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

  @staticmethod
  def longest_palindromic_subsequence(s1):
    s2 = s1[::-1]
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
          dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

  @staticmethod
  def edit_distance(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
      dp[i][0] = i
    for j in range(m + 1):
      dp[0][j] = j

    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = 1 + min(
            dp[i - 1][j],
            dp[i][j - 1],
            dp[i - 1][j - 1],
          )

    return dp[n][m]

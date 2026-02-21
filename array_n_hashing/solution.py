from collections import defaultdict
from typing import List


class Solution:
  @staticmethod
  def get_concatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * 2 * n
    for i in range(n):
      ans[i] = nums[i]
      ans[i + n] = nums[i]
    return ans

  @staticmethod
  def contains_duplicate(nums: List[int]) -> bool:
    nums_set = set()
    for n in nums:
      if n in nums_set:
        return True
      nums_set.add(n)
    return False

  @staticmethod
  def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    count = [0] * 26
    for char in s:
      c = ord(char) - ord('a')
      count[c % 26] += 1

    for char in t:
      c = ord(char) - ord('a')
      count[c % 26] -= 1
      if count[c % 26] < 0: return False
    return True

  @staticmethod
  # O(n) | O(n)
  def two_sum(nums: List[int], target: int) -> List[int]:
    ans = [0] * 2
    if len(nums) < 2: return ans

    lookup_map = {}
    for index, value in enumerate(nums):
      key = target - value
      if key in lookup_map:
        ans[0] = lookup_map[key]
        ans[1] = index
        return ans
      else:
        lookup_map[value] = index
    return ans

  @staticmethod
  # O(nlogn) | O(n)
  def longest_common_prefix(strs: List[str]) -> str:
    # Sort lexicographically compare first and last
    if len(strs) == 0: return ""
    lst = []
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
      if first[i] != last[i]: return "".join(lst)
      lst.append(first[i])
    return "".join(lst)

  @staticmethod
  def group_anagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord('a')] += 1
      res[tuple(count)].append(s)
    return list(res.values())

  @staticmethod
  def majority_element(nums: List[int]) -> int:
    count = 0
    res = 0
    for num in nums:
      if count == 0:
        res = num
      if res == num:
        count += 1
      else:
        count -= 1
    return res

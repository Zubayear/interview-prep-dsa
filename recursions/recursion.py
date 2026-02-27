from typing import List

# (n*2^n)
def subsets(nums: List[int]):
  res = []
  subset = []
  def dfs(i: int, n: int):
    if i >= n:
      res.append(subset.copy())
      return
    subset.append(nums[i])
    dfs(i+1, n)
    subset.pop()
    dfs(i+1, n)

  dfs(0, len(nums))
  return res

def subsetsII(nums):
  nums = sorted(nums)
  res = []
  subset = []
  def dfs(idx):
    res.append(subset.copy())
    for i in range(idx, len(nums)):
      if i > idx and nums[i] == nums[i-1]: continue
      subset.append(nums[i])
      dfs(i+1)
      subset.pop()
  dfs(0)
  return res

def combination_sum(nums, target):
  res = []
  subset = []
  def dfs(i, n, t):
    if t == 0:
      res.append(subset.copy())
      return
    if i >= n:
      return
    if nums[i] <= t:
      subset.append(nums[i])
      dfs(i, n, t-nums[i]) # i have chance to take that value again
      subset.pop()
    dfs(i+1, n, t)
    
  dfs(0, len(nums), target)
  return res

def combination_sumII(nums, target):
  nums = sorted(nums)
  res = []
  subset = []
  print(nums)
  def dfs(idx, t):
    if t == 0:
      res.append(subset.copy())
      return
    for i in range(idx, len(nums)):
      if i > idx and nums[i] == nums[i-1]: continue
      if nums[i] > t: break
      subset.append(nums[i])
      dfs(i+1, t-nums[i])
      subset.pop()
  dfs(0, target)
  return res

def combine(n, k):
  nums = [i for i in range(1, n+1)]
  res = []
  subset = []
  def dfs(idx):
    if len(subset) == k:
      res.append(subset.copy())
      return
    for i in range(idx, len(nums)):
      subset.append(nums[i])
      dfs(i+1)
      subset.pop()
      
  dfs(0)
  return res

def permute(nums):
  return None
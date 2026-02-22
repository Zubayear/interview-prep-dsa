from dp.solution import Solution


def test_tribonacci():
  assert Solution.tribonacci(4) == 4
  assert Solution.tribonacci(25) == 1389537


def test_rob():
  assert Solution.rob([1, 2, 3, 1]) == 4
  assert Solution.rob([2, 7, 9, 3, 1]) == 12

from recursions.recursion import subsets, combination_sum, combination_sumII, \
subsetsII, combine
from pytest_unordered import unordered


def test_subsets():
  assert subsets([1, 2, 3]) ==  unordered([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

def test_subsetII():
  assert subsetsII([1,2,1]) == unordered([[],[1],[1,1],[1,1,2],[1,2],[2]])
  assert subsetsII([7,2]) == unordered([[],[2],[2,7],[7]])

def test_combination_sum():
  assert combination_sum([2,5,6,9], 9) == unordered([[2,2,5], [9]])

def test_combination_sumII():
  assert combination_sumII([9,2,2,4,6,1,5], 8) == unordered([[1,2,5],[2,2,4],[2,6]])
  assert combination_sumII([1,2,3,4,5], 7) == unordered([[1,2,4],[2,5],[3,4]])

def test_combine():
  assert combine(4, 2) == unordered([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
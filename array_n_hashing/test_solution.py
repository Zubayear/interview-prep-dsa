from array_n_hashing.solution import Solution


def test_get_concatenation():
  assert Solution.get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]


def test_contains_duplicate():
  assert Solution.contains_duplicate([1, 2, 1, 1]) == True
  assert Solution.contains_duplicate([1, 2, 3, 4]) == False
  assert Solution.contains_duplicate([]) == False


def test_is_anagram():
  assert Solution.is_anagram("anagram", "nagaram") == True
  assert Solution.is_anagram("rat", "car") == False


def test_two_sum():
  assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
  assert Solution.two_sum([3, 2, 4], 6) == [1, 2]
  assert Solution.two_sum([3, 3], 6) == [0, 1]


def test_longest_common_prefix():
  assert Solution.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
  assert Solution.longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_majority_element():
  assert Solution.majority_element([3, 2, 3]) == 3
  assert Solution.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

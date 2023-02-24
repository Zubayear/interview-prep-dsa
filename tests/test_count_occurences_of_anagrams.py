from sliding_window.count_occurences_of_anagrams import count_anagram_occurances

def test_count_anagram_occurances():
    assert count_anagram_occurances('abc', 'cbaebabacd') == [0,6]